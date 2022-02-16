package main

import (
	"fmt"
	"io/ioutil"
	"strings"
)

func main() {

	// fmt.Println("Hello world!")

	dat, _ := ioutil.ReadFile("day_09_test.txt")
	// fmt.Print(string(dat))

	var s string
	s = string(dat)
	fmt.Println(s)

	var parts = strings.Split(s, ",")
	fmt.Println(parts)

	// // replace new line
	// s = strings.Replace(s, "\n", "", -1)

	// // initialize total
	// var total int = 0

	// // var len int = 10

	// // loop through string
	// for _, char := range s {
	// 	// var is_lowest bool = true
	// 	var current int = int(char)
	// 	fmt.Println(string(current))
	// 	fmt.Println(char)

	// 	// fmt.Printf(string(pos))
	// 	// if is_lowest {
	// 	total += (current + 1)
	// 	// total += 1
	// 	// }
	// }

	// // print result
	// fmt.Println(total)
}

// Each number corresponds to the height of a particular location, where 9 is
// the highest and 0 is the lowest a location can be.

// Your first goal is to find the low points - the locations that are lower than
// any of its adjacent locations. Most locations have four adjacent locations
// (up, down, left, and right); locations on the edge or corner of the map have
// three or two adjacent locations, respectively. (Diagonal locations do not count as adjacent.)

// In the above example, there are four low points, all highlighted: two are in
// the first row (a 1 and a 0), one is in the third row (a 5), and one is in the
// bottom row (also a 5). All other locations on the heightmap have some lower
// adjacent location, and so are not low points.

// The risk level of a low point is 1 plus its height. In the above example,
// the risk levels of the low points are 2, 1, 6, and 6. The sum of the risk
// levels of all low points in the heightmap is therefore 15.

// Find all of the low points on your heightmap. What is the sum of the risk
// levels of all low points on your heightmap?
