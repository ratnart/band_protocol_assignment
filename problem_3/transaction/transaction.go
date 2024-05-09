package transaction

import (
	"bytes"
	"encoding/json"
	"fmt"
	"net/http"
)

type Transaction struct {
}

type TransactionPipelineInput struct{
	Symbol    string `json:"symbol"`
	Price     uint64 `json:"price"`
	Timestamp uint64 `json:"timestamp"`
}

type TransactionPipelineOutput struct{
	TxStatus string `json:"tx_status"`
}

type BroadcastTransactionRequest struct {
	Symbol    string `json:"symbol"`
	Price     uint64 `json:"price"`
	Timestamp uint64 `json:"timestamp"`
}

type BroadcastTransactionResponse struct {
	TxHash string `json:"tx_hash"`
}

type MonitorTransactionStatusRequest struct {
	TxHash string `json:"tx_hash"`
}

type MonitorTransactionStatusResponse struct {
	TxStatus string `json:"tx_status"`
}

func (t Transaction) BroadcastTransaction(request BroadcastTransactionRequest) (BroadcastTransactionResponse,error) {
	jsonData,err:=json.Marshal(request)
	if err!=nil{
		return BroadcastTransactionResponse{} ,err
	}
	
	fmt.Printf("%s Broadcasting...\n",string(jsonData))
	req, err := http.NewRequest("POST", "https://mock-node-wgqbnxruha-as.a.run.app/broadcast", bytes.NewBuffer(jsonData))
	if err!=nil{
		return BroadcastTransactionResponse{} ,err
	}

	req.Header.Set("Content-Type","application/json")
	client:=&http.Client{}
	resp,err:=client.Do(req)
	if err!=nil{
		return BroadcastTransactionResponse{} ,err
	}
	defer resp.Body.Close()
	
	var response BroadcastTransactionResponse
	err=json.NewDecoder(resp.Body).Decode(&response)
	if err!=nil{
		return BroadcastTransactionResponse{} ,err
	}

	fmt.Printf("%s Broadcasting Successfully\n",string(jsonData))
	return response,err
}

func (t Transaction) MonitorTransactionStatus(request MonitorTransactionStatusRequest)(MonitorTransactionStatusResponse,error) {
	fmt.Printf("%s Monitoring...\n",request.TxHash)
	
	resp,err:=http.Get(fmt.Sprintf("https://mock-node-wgqbnxruha-as.a.run.app/check/%s",request.TxHash))
	if err!=nil{
		return MonitorTransactionStatusResponse{} ,err
	}
	defer resp.Body.Close()
	
	var response MonitorTransactionStatusResponse
	err=json.NewDecoder(resp.Body).Decode(&response)
	if err!=nil{
		return MonitorTransactionStatusResponse{} ,err
	}

	fmt.Printf("%s Monitoring Successfully\n",request.TxHash)
	return response,err
}

func (t Transaction) InvokeTransactionPipeline(pipelineInput TransactionPipelineInput)(TransactionPipelineOutput,error){
	broadcastRequest := BroadcastTransactionRequest(pipelineInput)

	resBroadcast,err:=t.BroadcastTransaction(BroadcastTransactionRequest(broadcastRequest))
	if(err!=nil){
		return TransactionPipelineOutput{},err
	}

	monitorRequest:=MonitorTransactionStatusRequest(resBroadcast)
	resTransaction,err:=t.MonitorTransactionStatus(MonitorTransactionStatusRequest(monitorRequest))

	return TransactionPipelineOutput(resTransaction),err
}