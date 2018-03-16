/* 
 * bank account
*/

var account = {
	balance: 0
}
// open account
function open(account, amount) {
	account.balance = amount;
}

//deposit to account
function deposit( account, amount ){
	account.balance = account.balance  + amount;
}
// withdraw
function withdraw(account, amount) {
	account.balance = account.balance - amount;
}

// amount of money in account
function getBalance( account ) {
	return account.balance;
}

deposit(account, 1000);
console.log('Balance = ' + getBalance(account));
deposit(account, 1000);
console.log('Balance = ' + getBalance(account));
withdraw(account, 120);
console.log('Balance = ' + getBalance(account));
