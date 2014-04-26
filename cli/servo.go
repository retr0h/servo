package main

import (
	"os"

	"github.com/codegangsta/cli"
	"github.com/retr0h/servo"
)

func main() {
	app := cli.NewApp()
	app.Name = "servo-cli"
	app.Usage = "CLI command for servo."
	app.Flags = []cli.Flag {
		cli.StringFlag{"action, a", "produce", "type of action to perform"},
	}
	app.Action = func(c *cli.Context) {
		if c.String("action") == "consume" {
			println("Consuming")
			servo.Cons()
		} else {
			println("Produce")
			servo.Prod()
		}
	}
	app.Run(os.Args)
}
