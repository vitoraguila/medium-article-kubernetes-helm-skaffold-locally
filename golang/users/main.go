package main

import (
	"encoding/json"
	"net/http"
)

func main() {

	http.HandleFunc("/api/golang/users", HandleGetVideos)

	http.ListenAndServe(":8080", nil)
}

func HandleGetVideos(w http.ResponseWriter, r *http.Request) {

	videos := getUsers()

	videoBytes, err := json.Marshal(videos)

	if err != nil {
		panic(err)
	}

	w.Write(videoBytes)
}
