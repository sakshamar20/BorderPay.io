package chaincode

import (
	"encoding/json"
	"fmt"

	"github.com/hyperledger/fabric-contract-api-go/contractapi"
)

// SmartContract provides functions for managing an Asset
type SmartContract struct {
	contractapi.Contract
}

var (
    Local_tax float32 = 1.0
    cross_border float32 = 0.8
	forex_rate float32 = 4.0
	routing float32 = 0.5
)

const (
    rupeeToDollar = 0.014
    rupeeToEuro   = 0.012
    dollarToRupee = 72.0
    dollarToEuro  = 0.85
    euroToRupee   = 88.5
    euroToDollar  = 1.18
)

// Asset describes basic details of what makes up a simple asset
// Insert struct field in alphabetic order => to achieve determinism across languages
// golang keeps the order when marshal to json but doesn't order automatically
type Asset struct {
	Account		   string    `json:"Account"`
	Name          string `json:"Name"`
	Balance        int `json:"Balance"`
	Bank          string `json:"Bank"`
	Denom          string    `json:"Denom"`
	Loca		string `json:"Loca"`
}

// InitLedger adds a base set of assets to the ledger
func (s *SmartContract) InitLedger(ctx contractapi.TransactionContextInterface) error {
	assets := []Asset{
		{Account: "23456", Name: "Optiver", Balance: 100000000, Bank: "b", Denom: "dollar", Loca: "USA"},
		{Account: "34567", Name: "Google", Balance: 100000000, Bank: "c", Denom: "euro", Loca: "Netherlands"},
		{Account: "45678", Name: "Oracle", Balance: 100000000, Bank: "a", Denom: "dollar", Loca: "Canada"},
		{Account: "56789", Name: "EXL", Balance: 100000000, Bank: "b", Denom: "dollar", Loca: "Australia"},
		{Account: "67890", Name: "Aryan", Balance: 100, Bank: "c", Denom: "rupees", Loca: "India"},
		{Account: "78901", Name: "Saksham", Balance: 100, Bank: "a", Denom: "dollar", Loca: "USA"},
		{Account: "89012", Name: "Shubham", Balance: 100, Bank: "b", Denom: "euro", Loca: "Netherlands"},
		{Account: "90123", Name: "Sachin", Balance: 100, Bank: "c", Denom: "dollar", Loca: "Canada"},
		{Account: "12345", Name: "Ujwal", Balance: 100, Bank: "a", Denom: "dollar", Loca: "Australia"},
	}

	for _, asset := range assets {
		assetJSON, err := json.Marshal(asset)
		if err != nil {
			return err
		}

		err = ctx.GetStub().PutState(asset.Account, assetJSON)
		if err != nil {
			return fmt.Errorf("failed to put to world state. %v", err)
		}
	}

	return nil
}

// CreateAsset issues a new asset to the world state with given details.
func (s *SmartContract) CreateAsset(ctx contractapi.TransactionContextInterface, Account string, Name string, Balance int, Bank string, Denom string, Loca string) error {
	exists, err := s.AssetExists(ctx, Account)
	if err != nil {
		return err
	}
	if exists {
		return fmt.Errorf("the asset %s already exists", Account)
	}

	asset := Asset{
		Account:             Account,
		Name:          Name,
		Balance:           Balance,
		Bank:          Bank,
		Denom: Denom,
		Loca: Loca, 
	}
	assetJSON, err := json.Marshal(asset)
	if err != nil {
		return err
	}

	return ctx.GetStub().PutState(Account, assetJSON)
}

// ReadAsset returns the asset stored in the world state with given id.
func (s *SmartContract) ReadAsset(ctx contractapi.TransactionContextInterface, Account string) (*Asset, error) {
	assetJSON, err := ctx.GetStub().GetState(Account)
	if err != nil {
		return nil, fmt.Errorf("failed to read from world state: %v", err)
	}
	if assetJSON == nil {
		return nil, fmt.Errorf("the asset %s does not exist", Account)
	}

	var asset Asset
	err = json.Unmarshal(assetJSON, &asset)
	if err != nil {
		return nil, err
	}

	return &asset, nil
}

// UpdateAsset updates an existing asset in the world state with provided parameters.
func (s *SmartContract) UpdateAsset(ctx contractapi.TransactionContextInterface,Account string, Name string, Balance int, Bank string, Denom string, Loca string) error {
	exists, err := s.AssetExists(ctx, Account)
	if err != nil {
		return err
	}
	if !exists {
		return fmt.Errorf("the asset %s does not exist", Account)
	}

	// overwriting original asset with new asset
	asset := Asset{
		Account:             Account,
		Name:          		 Name,
		Balance:             Balance,
		Bank:                Bank,
		Denom:				 Denom,
		Loca: 				 Loca, 
	}
	assetJSON, err := json.Marshal(asset)
	if err != nil {
		return err
	}

	return ctx.GetStub().PutState(Account, assetJSON)
}

// DeleteAsset deletes an given asset from the world state.
func (s *SmartContract) DeleteAsset(ctx contractapi.TransactionContextInterface, Account string) error {
	exists, err := s.AssetExists(ctx, Account)
	if err != nil {
		return err
	}
	if !exists {
		return fmt.Errorf("the asset %s does not exist", Account)
	}

	return ctx.GetStub().DelState(Account)
}

// AssetExists returns true when asset with given ID exists in world state
func (s *SmartContract) AssetExists(ctx contractapi.TransactionContextInterface, Account string) (bool, error) {
	assetJSON, err := ctx.GetStub().GetState(Account)
	if err != nil {
		return false, fmt.Errorf("failed to read from world state: %v", err)
	}

	return assetJSON != nil, nil
}

func forex(fromCurrency string, toCurrency string) float32 {
    switch fromCurrency {
    case "rupees":
        switch toCurrency {
        case "dollar":
            return rupeeToDollar
        case "euro":
            return rupeeToEuro
        default:
            return 1.0 // No conversion needed
        }
    case "dollar":
        switch toCurrency {
        case "rupees":
            return dollarToRupee
        case "euro":
            return dollarToEuro
        default:
            return 1.0 // No conversion needed
        }
    case "euro":
        switch toCurrency {
        case "rupees":
            return euroToRupee
        case "dollar":
            return euroToDollar
        default:
            return 1.0 // No conversion needed
        }
    default:
        return 1.0 // No conversion needed
    }
}



// TransferAsset updates the owner field of asset with given id in world state, and returns the old owner.
func (s *SmartContract) TransferAsset(ctx contractapi.TransactionContextInterface, acc1 string, acc2 string, amount int) (bool, error) {
	asset1, err := s.ReadAsset(ctx, acc1)
	if err != nil {
		return false, err
	}

	asset2, err := s.ReadAsset(ctx, acc2)
	if err != nil {
		return false, err
	}



	if asset1.Balance < amount {
		errMsg := "Insufficent funds in bank reserves: " + asset1.Name + " Bank Account: " + asset1.Account
		return false ,fmt.Errorf(errMsg)
	}

	if asset1.Loca == asset2.Loca {
		asset2.Balance = asset2.Balance + amount
		if asset1.Bank == asset2.Bank {
			asset1.Balance = asset1.Balance - amount
		} else {
			asset1.Balance = asset1.Balance - int(float32(amount) * (1 + 0.01 * Local_tax))
		}
	} else {
		convertedAmount := float32(amount) * forex(asset1.Denom, asset2.Denom)
		asset1.Balance = asset1.Balance - int((1 + 0.01 * forex_rate) * float32(amount))
		asset2.Balance = asset2.Balance + int(convertedAmount * (1 - 0.01 * (cross_border + routing)))
	}
	



	assetJSON, err := json.Marshal(asset1)
	if err != nil {
		return false, err
	}

	err = ctx.GetStub().PutState(asset1.Account, assetJSON)
	if err != nil {
		return false, err
	}

	assetJSON2, err := json.Marshal(asset2)
	if err != nil {
		return false, err
	}

	err = ctx.GetStub().PutState(asset2.Account, assetJSON2)
	if err != nil {
		return false, err
	}

	return true, nil
}

// GetAllAssets returns all assets found in world state
func (s *SmartContract) GetAllAssets(ctx contractapi.TransactionContextInterface) ([]*Asset, error) {
	// range query with empty string for startKey and endKey does an
	// open-ended query of all assets in the chaincode namespace.
	resultsIterator, err := ctx.GetStub().GetStateByRange("", "")
	if err != nil {
		return nil, err
	}
	defer resultsIterator.Close()

	var assets []*Asset
	for resultsIterator.HasNext() {
		queryResponse, err := resultsIterator.Next()
		if err != nil {
			return nil, err
		}

		var asset Asset
		err = json.Unmarshal(queryResponse.Value, &asset)
		if err != nil {
			return nil, err
		}
		assets = append(assets, &asset)
	}

	return assets, nil
}
