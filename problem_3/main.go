package main

import (
	"bandProtocol/transaction"
	"fmt"
	"sync"
)

type input struct{
	symbol string
	price uint64
	timestamp uint64
}

func display(transaction input,status transaction.TransactionStatus){
	fmt.Printf("------\nsymbol:%s\nprice:%d\ntimestamp:%d\nstatus:%s\n------\n",transaction.symbol,transaction.price,transaction.timestamp,status)
}

func main() {

	inputList:= []input{
		{
			symbol: "ETH",
			price:4500,
			timestamp: 1678912345,
		},
		{
			symbol: "ETH",
			price:4200,
			timestamp: 1678912345,
		},
		{
			symbol: "ETH",
			price:4300,
			timestamp: 1678912345,
		},
		{
			symbol: "ETH",
			price:4400,
			timestamp: 1678912345,
		},
	}

	transactionModule := transaction.Transaction{}
	var wg sync.WaitGroup
	
	for _,input:= range inputList{
		go func(){
			response,err:= transactionModule.InvokeTransactionPipeline(transaction.TransactionPipelineInput{Symbol:input.symbol,Price: input.price,Timestamp: input.timestamp})
			if err!=nil{
				fmt.Println(err)
			}else{
				display(input,response.TxStatus)
				switch response.TxStatus{
					case transaction.CONFIRMED:
						//Notify the user that transaction is completed
					case transaction.FAILED:
						//Notify the user that transaction has failed to process
					case transaction.PENDING:
						//Notify the user that transaction is currently being processed
					case transaction.DNE:
						//Notify the user that transaction does not exist
					default:
						fmt.Println("Wrong Transaction Status")
				}
			}
			wg.Done()
		}()
		wg.Add(1)
	}
	wg.Wait()
	fmt.Println("Process Succesfully")
}
