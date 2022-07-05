package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	reader := bufio.NewReader(os.Stdin)
	fmt.Print("Welcome to Golang Live Coding\n1. Palindrome\n2. Anagram\nEnter menu: ")
	text, err := reader.ReadString('\n')
	if err != nil {
		fmt.Printf("There's an error %+d", err)
	}
	fmt.Printf("Your input is: %s", text)
}
