package main

import (
	"fmt"
	"net"
)

const (
	SERVER_HOST = "localhost"
	SERVER_PORT = "8000"
	SERVER_TYPE = "tcp"
)

func main() {
	connection, err := net.Dial(SERVER_TYPE, SERVER_HOST+":"+SERVER_PORT)
	if err != nil {
		panic(err)
	}
	buffer := make([]byte, 1024)
	var quest string
	var resp string

	for {
		fmt.Print("De 1 a 9, qual questão você deseja testar?\n")
		fmt.Scanln(&quest)
		connection.Write([]byte(quest))

		if quest == "0" {
			fmt.Println("Conexão encerrada!")
			connection.Close()
			break
		}

		mLen, err := connection.Read(buffer)
		if err != nil {
			fmt.Println("Error reading:", err.Error())
		}

		resp = string(buffer[:mLen])
		if resp == "404 not found" {
			fmt.Println(resp)
			continue
		}

		for resp != "processing" {
			fmt.Println(resp)
			fmt.Scanln(&quest)
			connection.Write([]byte(quest))
			mLen, err = connection.Read(buffer)
			resp = string(buffer[:mLen])
		}

		mLen, err = connection.Read(buffer)
		resp = string(buffer[:mLen])
		fmt.Println(resp)
	}
}
