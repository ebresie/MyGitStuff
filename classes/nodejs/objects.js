//object is key value collection
var person = {
	gender: 'male',
	'eyeColor': 'brown'
};
person['firstName'] = 'Eric';
person['lastName'] = 'Bresie';
person.age = 49;

function greetUser( person ) {
	console.log('Hello ' + person.firstName + ' ' + person.lastName);	
}

greetUser(person);

var pet = {
	name: 'name',
	type: 'petType'
}

function printPet( pet ) {
	console.log( 'Your ' + pet.type + ' is named ' + pet.name);
}

printPet(pet);