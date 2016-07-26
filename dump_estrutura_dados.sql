--
-- PostgreSQL database dump
--

-- Dumped from database version 9.3.12
-- Dumped by pg_dump version 9.3.12
-- Started on 2016-04-15 09:58:17 BRT

SET statement_timeout = 0;
SET lock_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SET check_function_bodies = false;
SET client_min_messages = warning;

--
-- TOC entry 2038 (class 1262 OID 16909)
-- Dependencies: 2037
-- Name: chaves; Type: COMMENT; Schema: -; Owner: postgres
--

COMMENT ON DATABASE chaves IS 'banco de dados sistema chaves.';


--
-- TOC entry 1 (class 3079 OID 11791)
-- Name: plpgsql; Type: EXTENSION; Schema: -; Owner: 
--

CREATE EXTENSION IF NOT EXISTS plpgsql WITH SCHEMA pg_catalog;


--
-- TOC entry 2041 (class 0 OID 0)
-- Dependencies: 1
-- Name: EXTENSION plpgsql; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION plpgsql IS 'PL/pgSQL procedural language';


SET search_path = public, pg_catalog;

--
-- TOC entry 192 (class 1255 OID 16910)
-- Name: remove_acento(text); Type: FUNCTION; Schema: public; Owner: postgres
--

CREATE FUNCTION remove_acento(text) RETURNS text
    LANGUAGE sql IMMUTABLE STRICT
    AS $_$
SELECT TRANSLATE($1,'áàãâäÁÀÃÂÄéèêëÉÈÊËíìîïÍÌÎÏóòõôöÓÒÕÔÖúùûüÚÙÛÜñÑçÇÿýÝ','aaaaaAAAAAeeeeEEEEiiiiIIIIoooooOOOOOuuuuUUUUnNcCyyY')
$_$;


ALTER FUNCTION public.remove_acento(text) OWNER TO postgres;

--
-- TOC entry 2042 (class 0 OID 0)
-- Dependencies: 192
-- Name: FUNCTION remove_acento(text); Type: COMMENT; Schema: public; Owner: postgres
--

COMMENT ON FUNCTION remove_acento(text) IS 'Remove letras com acentuação';


--
-- TOC entry 171 (class 1259 OID 16911)
-- Name: seq_id_auto; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE seq_id_auto
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    MAXVALUE 9999
    CACHE 1
    CYCLE;


ALTER TABLE public.seq_id_auto OWNER TO postgres;

SET default_tablespace = '';

SET default_with_oids = false;

--
-- TOC entry 172 (class 1259 OID 16913)
-- Name: autos; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE autos (
    id integer DEFAULT nextval('seq_id_auto'::regclass) NOT NULL,
    sala_id integer NOT NULL,
    usuario_id integer NOT NULL,
    login_id integer NOT NULL
);


ALTER TABLE public.autos OWNER TO postgres;

--
-- TOC entry 173 (class 1259 OID 16917)
-- Name: seq_id_chave; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE seq_id_chave
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    MAXVALUE 9999
    CACHE 1
    CYCLE;


ALTER TABLE public.seq_id_chave OWNER TO postgres;

--
-- TOC entry 174 (class 1259 OID 16919)
-- Name: chaves; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE chaves (
    id integer DEFAULT nextval('seq_id_chave'::regclass) NOT NULL,
    nro_copia integer NOT NULL,
    sala_id integer NOT NULL
);


ALTER TABLE public.chaves OWNER TO postgres;

--
-- TOC entry 175 (class 1259 OID 16923)
-- Name: seq_id_login; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE seq_id_login
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    MAXVALUE 9999
    CACHE 1
    CYCLE;


ALTER TABLE public.seq_id_login OWNER TO postgres;

--
-- TOC entry 176 (class 1259 OID 16925)
-- Name: logins; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE logins (
    login character(20) NOT NULL,
    senha character(32) NOT NULL,
    nivel integer NOT NULL,
    nome character(40),
    id integer DEFAULT nextval('seq_id_login'::regclass) NOT NULL,
    ativo boolean
);


ALTER TABLE public.logins OWNER TO postgres;

--
-- TOC entry 2043 (class 0 OID 0)
-- Dependencies: 176
-- Name: TABLE logins; Type: COMMENT; Schema: public; Owner: postgres
--

COMMENT ON TABLE logins IS 'login para sistema';


--
-- TOC entry 2044 (class 0 OID 0)
-- Dependencies: 176
-- Name: COLUMN logins.nivel; Type: COMMENT; Schema: public; Owner: postgres
--

COMMENT ON COLUMN logins.nivel IS '1 - nivel baixo, 2 - nivel alto';


--
-- TOC entry 177 (class 1259 OID 16929)
-- Name: seq_id_predio; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE seq_id_predio
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    MAXVALUE 9999
    CACHE 1
    CYCLE;


ALTER TABLE public.seq_id_predio OWNER TO postgres;

--
-- TOC entry 178 (class 1259 OID 16931)
-- Name: predios; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE predios (
    id integer DEFAULT nextval('seq_id_predio'::regclass) NOT NULL,
    nome character(40)
);


ALTER TABLE public.predios OWNER TO postgres;

--
-- TOC entry 2045 (class 0 OID 0)
-- Dependencies: 178
-- Name: TABLE predios; Type: COMMENT; Schema: public; Owner: postgres
--

COMMENT ON TABLE predios IS 'predios';


--
-- TOC entry 179 (class 1259 OID 16935)
-- Name: seq_id_retirada; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE seq_id_retirada
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    MAXVALUE 9999
    CACHE 1
    CYCLE;


ALTER TABLE public.seq_id_retirada OWNER TO postgres;

--
-- TOC entry 180 (class 1259 OID 16937)
-- Name: retiradas; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE retiradas (
    id integer DEFAULT nextval('seq_id_retirada'::regclass) NOT NULL,
    login_id integer NOT NULL,
    chave_id integer NOT NULL,
    usuario_id integer NOT NULL,
    datahora_ent timestamp without time zone NOT NULL,
    datahora_rec timestamp without time zone
);


ALTER TABLE public.retiradas OWNER TO postgres;

--
-- TOC entry 181 (class 1259 OID 16941)
-- Name: seq_id_sala; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE seq_id_sala
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    MAXVALUE 9999
    CACHE 1
    CYCLE;


ALTER TABLE public.seq_id_sala OWNER TO postgres;

--
-- TOC entry 182 (class 1259 OID 16943)
-- Name: salas; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE salas (
    id integer DEFAULT nextval('seq_id_sala'::regclass) NOT NULL,
    nome character(10),
    predio_id integer,
    direito character(1),
    horario_min character(5),
    horario_max character(5)
);


ALTER TABLE public.salas OWNER TO postgres;

--
-- TOC entry 2046 (class 0 OID 0)
-- Dependencies: 182
-- Name: COLUMN salas.direito; Type: COMMENT; Schema: public; Owner: postgres
--

COMMENT ON COLUMN salas.direito IS 'a - para alunos e prof | p - para prof somente';


--
-- TOC entry 183 (class 1259 OID 16947)
-- Name: seq_id_usuario; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE seq_id_usuario
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    MAXVALUE 9999
    CACHE 1
    CYCLE;


ALTER TABLE public.seq_id_usuario OWNER TO postgres;

--
-- TOC entry 184 (class 1259 OID 16949)
-- Name: teste; Type: VIEW; Schema: public; Owner: postgres
--

CREATE VIEW teste AS
 SELECT (((((l.nome)::text || ' - '::text) || (s.nome)::text) || ' - '::text) || to_char(r.datahora_ent, 'DD/MM/YYYY'::text))
   FROM logins l,
    retiradas r,
    salas s
  WHERE (((l.id = r.login_id) AND (s.id = r.chave_id)) AND (r.datahora_rec IS NULL));


ALTER TABLE public.teste OWNER TO postgres;

--
-- TOC entry 185 (class 1259 OID 16953)
-- Name: usuarios; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE usuarios (
    id integer DEFAULT nextval('seq_id_usuario'::regclass) NOT NULL,
    nome character(40) NOT NULL,
    cod_barra integer,
    email character(60),
    cpf character(15),
    tipo character(1)
);


ALTER TABLE public.usuarios OWNER TO postgres;

--
-- TOC entry 2047 (class 0 OID 0)
-- Dependencies: 185
-- Name: COLUMN usuarios.tipo; Type: COMMENT; Schema: public; Owner: postgres
--

COMMENT ON COLUMN usuarios.tipo IS 'a - para alunos| p - para prof somente';


--
-- TOC entry 2020 (class 0 OID 16913)
-- Dependencies: 172
-- Data for Name: autos; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY autos (id, sala_id, usuario_id, login_id) FROM stdin;
\.


--
-- TOC entry 2022 (class 0 OID 16919)
-- Dependencies: 174
-- Data for Name: chaves; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY chaves (id, nro_copia, sala_id) FROM stdin;
\.


--
-- TOC entry 2024 (class 0 OID 16925)
-- Dependencies: 176
-- Data for Name: logins; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY logins (login, senha, nivel, nome, id, ativo) FROM stdin;
admin               	21232f297a57a5a743894a0e4a801fc3	2	Admin                                   	1	\N
\.


--
-- TOC entry 2026 (class 0 OID 16931)
-- Dependencies: 178
-- Data for Name: predios; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY predios (id, nome) FROM stdin;
\.


--
-- TOC entry 2028 (class 0 OID 16937)
-- Dependencies: 180
-- Data for Name: retiradas; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY retiradas (id, login_id, chave_id, usuario_id, datahora_ent, datahora_rec) FROM stdin;
\.


--
-- TOC entry 2030 (class 0 OID 16943)
-- Dependencies: 182
-- Data for Name: salas; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY salas (id, nome, predio_id, direito, horario_min, horario_max) FROM stdin;
\.


--
-- TOC entry 2048 (class 0 OID 0)
-- Dependencies: 171
-- Name: seq_id_auto; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('seq_id_auto', 1, false);


--
-- TOC entry 2049 (class 0 OID 0)
-- Dependencies: 173
-- Name: seq_id_chave; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('seq_id_chave', 1, false);


--
-- TOC entry 2050 (class 0 OID 0)
-- Dependencies: 175
-- Name: seq_id_login; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('seq_id_login', 1, true);


--
-- TOC entry 2051 (class 0 OID 0)
-- Dependencies: 177
-- Name: seq_id_predio; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('seq_id_predio', 1, false);


--
-- TOC entry 2052 (class 0 OID 0)
-- Dependencies: 179
-- Name: seq_id_retirada; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('seq_id_retirada', 1, false);


--
-- TOC entry 2053 (class 0 OID 0)
-- Dependencies: 181
-- Name: seq_id_sala; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('seq_id_sala', 1, false);


--
-- TOC entry 2054 (class 0 OID 0)
-- Dependencies: 183
-- Name: seq_id_usuario; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('seq_id_usuario', 1, false);


--
-- TOC entry 2032 (class 0 OID 16953)
-- Dependencies: 185
-- Data for Name: usuarios; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY usuarios (id, nome, cod_barra, email, cpf, tipo) FROM stdin;
\.


--
-- TOC entry 2040 (class 0 OID 0)
-- Dependencies: 7
-- Name: public; Type: ACL; Schema: -; Owner: postgres
--

REVOKE ALL ON SCHEMA public FROM PUBLIC;
REVOKE ALL ON SCHEMA public FROM postgres;
GRANT ALL ON SCHEMA public TO postgres;
GRANT ALL ON SCHEMA public TO PUBLIC;


-- Completed on 2016-04-15 09:58:17 BRT

--
-- PostgreSQL database dump complete
--

