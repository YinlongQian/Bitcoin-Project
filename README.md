Bitcoin Project
---

Each row from the txin.dat file is called a transaction input. Each row from the txout.dat file is called a transaction output.  
  
A single transaction is composed of transaction inputs and transaction outputs. These share a common transaction id(txID). Each input is associated with one output. I was first confused when I saw that there can be multiple input/output pairs, so I will provide an example and try to define some terms.  
  
I want to send .25 Bitcoin to someone but all I have is a whole Bitcoin in my possession. So I will send .25 Bitcoin to the person of my choice. And then I will send .75 Bitcoin back to myself, as change. This will create 2 input/output pairs in my transaction. One going to the original recipient, and the other going back to myself as change.  
  
The address id(addrID) represents the new owner of the money, when I use the word, "someone", or "myself" in the previous example I ment addrIDs.  
  
Each input contains a reference to the output it is using. This is stored in the previous transaction id(prev_txID). 
  
Users money is stored in the form of unspent transaction outputs(txout.dat). In order to find the value of someones you would count the unspent outputs that share an addrID of the individual. An unspent output is one where there is no input which references it in its prev_txID.   
  
[Here](https://en.bitcoin.it/wiki/Transaction#Input) is another explanation if mine was lacking.
