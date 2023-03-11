package main

import "fmt"

func main() {
	var p *int = nil
	fmt.Println("before accessing illegal access")
	*p = 0
	fmt.Println("after accessing illegal access")
}
