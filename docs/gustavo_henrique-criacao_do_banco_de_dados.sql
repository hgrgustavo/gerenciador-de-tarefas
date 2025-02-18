create database `database_gerenciador_tarefas`;
use `database_gerenciador_tarefas`;

create table `usuario` (
	`id` int primary key not null auto_increment,
    `nome` varchar(255) not null,
	`email` varchar(255) not null,
    check (`email` regexp '^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$')
);

create table `tarefa` (
	`id` int primary key not null auto_increment,
    `usuario_id` int not null,
    `descricao` varchar(255) not null,
	`setor` varchar(255) not null,
    `prioridade` enum('baixa', 'media', 'alta') not null,
    `data_cadastro` date,
    `status` enum('a fazer', 'fazendo', 'pronto') not null default 'a fazer',
    
    foreign key (`usuario_id`)
		references `usuario`(`id`)
);

