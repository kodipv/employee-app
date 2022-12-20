begin;

create table employees (
    id serial primary key,
    first_name text not null,
    last_name text not null,
    middle_name text not null,
    employment_date date not null default now(),
    manager_id int references employees (id)
);

create table positions (
    id serial primary key,
    name text not null unique
);

create table employee_positions (
    id serial primary key,
    employee_id int not null references employees (id),
    position_id int not null references positions (id),
    start_date date not null default now()::date,
    end_date date
);

create table employee_rates (
    id serial primary key,
    employee_id int not null references employees (id),
    monthly_rate int not null,
    start_date date not null default now()::date,
    end_date date
);


insert into employees (first_name, last_name, middle_name, employment_date, manager_id)
values
('Jack', 'Smith', 'Smithovich', '2022-01-01', null),
('Petr', 'Petrov', 'Petrovich', '2022-01-01', null),
('Ivan', 'Ivanov', 'Ivanovich', '2022-01-01', 1),
('Petr', 'Petrov', 'Petrovich', '2022-01-01', 6),
('Ignat', 'Ignatov', 'Ignatocich', '2022-01-01', 3),
('Wayne', 'Rooney', 'Manchesterovich', '2022-01-01', 1),
('Petr', 'Petrov', 'Petrovich', '2022-01-01', 3),
('Ignat', 'Ignatov', 'Ignatocich', '2022-01-01', 1);

insert into positions (name) values ('Продакт менежер');
insert into positions (name) values ('Разработчик');
insert into positions (name) values ('Тестировщик');

insert into employee_positions (employee_id, position_id) values (1, 1);
insert into employee_positions (employee_id, position_id) values (2, 1);
insert into employee_positions (employee_id, position_id) values (3, 2);
insert into employee_positions (employee_id, position_id) values (4, 3);
insert into employee_positions (employee_id, position_id) values (5, 3);
insert into employee_positions (employee_id, position_id) values (6, 2);
insert into employee_positions (employee_id, position_id) values (7, 3);
insert into employee_positions (employee_id, position_id) values (8, 2);

insert into employee_rates (employee_id, monthly_rate) values (1, 30000);
insert into employee_rates (employee_id, monthly_rate) values (2, 40000);
insert into employee_rates (employee_id, monthly_rate) values (3, 50000);
insert into employee_rates (employee_id, monthly_rate) values (4, 60000);
insert into employee_rates (employee_id, monthly_rate) values (5, 70000);
insert into employee_rates (employee_id, monthly_rate) values (6, 50000);
insert into employee_rates (employee_id, monthly_rate) values (7, 60000);
insert into employee_rates (employee_id, monthly_rate) values (8, 70000);

commit;