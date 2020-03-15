DROP TABLE public.beans;

CREATE TABLE public.beans (
	id serial NOT NULL,
	"name" varchar(50) NOT NULL,
	sku varchar(20) NOT NULL,
	qty int4 NULL DEFAULT 0,
	created_on timestamp NULL DEFAULT now(),
	CONSTRAINT beans_pkey PRIMARY KEY (id)
);

INSERT INTO public.beans ("name",sku,qty,created_on) VALUES 
('Dark Chocolate','drk-choco',3,'2020-03-15 15:43:07.225')
,('Black Forest','blk-frts',11,'2020-03-15 15:42:08.414')
;