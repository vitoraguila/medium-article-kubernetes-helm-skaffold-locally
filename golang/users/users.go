package main

import (
	"encoding/json"
	"io/ioutil"
)

type user struct {
	CustomerID string
	FirstName  string
	LastName   string
}

func getUsers() (users []user) {

	fileBytes, err := ioutil.ReadFile("./users.json")

	if err != nil {
		panic(err)
	}

	err = json.Unmarshal(fileBytes, &users)

	if err != nil {
		panic(err)
	}

	return users
}
