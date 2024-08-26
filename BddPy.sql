create database tienda;

use tienda;

create table productos(
	idProducto int auto_increment primary key,
	proCodigo int,
	proNombre varchar(100),
	proPrecio int,
	proCategoria varchar(100)
);

select * from productos;