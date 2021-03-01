db = db.getSiblingDB("cars_db");
db.car_tb.drop();

db.car_tb.insertMany([
    {
        "id": 1,
        "brand": "Ford",
        "model": "Mustang"
    },
    {
        "id": 2,
        "brand": "Lamborghini",
        "model": "Veneno"
    },
    {
        "id": 3,
        "brand": "Ferrari",
        "model": "Enzo"
    },
    {
        "id": 4,
        "brand": "Mercedes",
        "model": "Cls63-AMG"
    },
]);