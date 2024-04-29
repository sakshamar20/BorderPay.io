// yet to be completed

package main

import (
	"errors"
	"fmt"
)

type MyChaincode struct {
}

func main() {
	err := shim.Start(new(MyChaincode))
	if err != nil {
		fmt.Printf("Error starting chaincode: %s", err)
	}
}

func (t *MyChaincode) Init(stub shim.ChaincodeStubInterface, function string, args []string) ([]byte, error) {
	if len(args) != 1 {
		return nil, errors.New("Incorrect number of arguments. Expecting 1")
	}

	organizationType := args[0]
	switch organizationType {
	case "bank":
	case "organization":
	case "peer":
	default:
		return nil, errors.New("Unknown organization type")
	}

	return nil, nil
}

func (t *MyChaincode) Invoke(stub shim.ChaincodeStubInterface, function string, args []string) ([]byte, error) {
	switch function {
	case "init":
		return t.Init(stub, "init", args)
	case "someFunction":
	default:
		return nil, errors.New("Received unknown function invocation: " + function)
	}
}

func (t *MyChaincode) Query(stub shim.ChaincodeStubInterface, function string, args []string) ([]byte, error) {
	switch function {
	case "getSomething":
		return []byte("Something"), nil
	case "anotherQuery":
	default:
		return nil, errors.New("Received unknown function query: " + function)
	}
}
