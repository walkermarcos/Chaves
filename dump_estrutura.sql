--
-- PostgreSQL database dump
--

-- Dumped from database version 9.3.12
-- Dumped by pg_dump version 9.3.12
-- Started on 2016-04-15 08:15:14 BRT

SET statement_timeout = 0;
SET lock_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SET check_function_bodies = false;
SET client_min_messages = warning;

--
-- TOC entry 2063 (class 1262 OID 16750)
-- Dependencies: 2062
-- Name: chaves; Type: COMMENT; Schema: -; Owner: postgres
--

COMMENT ON DATABASE chaves IS 'banco de dados sistema chaves.';


--
-- TOC entry 1 (class 3079 OID 11791)
-- Name: plpgsql; Type: EXTENSION; Schema: -; Owner: 
--

CREATE EXTENSION IF NOT EXISTS plpgsql WITH SCHEMA pg_catalog;


--
-- TOC entry 2066 (class 0 OID 0)
-- Dependencies: 1
-- Name: EXTENSION plpgsql; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION plpgsql IS 'PL/pgSQL procedural language';


SET search_path = public, pg_catalog;

--
-- TOC entry 192 (class 1255 OID 16751)
-- Name: remove_acento(text); Type: FUNCTION; Schema: public; Owner: postgres
--

CREATE FUNCTION remove_acento(text) RETURNS text
    LANGUAGE sql IMMUTABLE STRICT
    AS $_$
SELECT TRANSLATE($1,'áàãâäÁÀÃÂÄéèêëÉÈÊËíìîïÍÌÎÏóòõôöÓÒÕÔÖúùûüÚÙÛÜñÑçÇÿýÝ','aaaaaAAAAAeeeeEEEEiiiiIIIIoooooOOOOOuuuuUUUUnNcCyyY')
$_$;


ALTER FUNCTION public.remove_acento(text) OWNER TO postgres;

--
-- TOC entry 2067 (class 0 OID 0)
-- Dependencies: 192
-- Name: FUNCTION remove_acento(text); Type: COMMENT; Schema: public; Owner: postgres
--

COMMENT ON FUNCTION remove_acento(text) IS 'Remove letras com acentuação';


--
-- TOC entry 171 (class 1259 OID 16752)
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
-- TOC entry 172 (class 1259 OID 16754)
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
-- TOC entry 173 (class 1259 OID 16758)
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
-- TOC entry 174 (class 1259 OID 16760)
-- Name: chaves; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE chaves (
    id integer DEFAULT nextval('seq_id_chave'::regclass) NOT NULL,
    nro_copia integer NOT NULL,
    sala_id integer NOT NULL
);


ALTER TABLE public.chaves OWNER TO postgres;

--
-- TOC entry 175 (class 1259 OID 16764)
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
-- TOC entry 176 (class 1259 OID 16766)
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
-- TOC entry 2068 (class 0 OID 0)
-- Dependencies: 176
-- Name: TABLE logins; Type: COMMENT; Schema: public; Owner: postgres
--

COMMENT ON TABLE logins IS 'login para sistema';


--
-- TOC entry 2069 (class 0 OID 0)
-- Dependencies: 176
-- Name: COLUMN logins.nivel; Type: COMMENT; Schema: public; Owner: postgres
--

COMMENT ON COLUMN logins.nivel IS '1 - nivel baixo, 2 - nivel alto';


--
-- TOC entry 177 (class 1259 OID 16770)
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
-- TOC entry 178 (class 1259 OID 16772)
-- Name: predios; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE predios (
    id integer DEFAULT nextval('seq_id_predio'::regclass) NOT NULL,
    nome character(40)
);


ALTER TABLE public.predios OWNER TO postgres;

--
-- TOC entry 2070 (class 0 OID 0)
-- Dependencies: 178
-- Name: TABLE predios; Type: COMMENT; Schema: public; Owner: postgres
--

COMMENT ON TABLE predios IS 'predios';


--
-- TOC entry 179 (class 1259 OID 16776)
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
-- TOC entry 180 (class 1259 OID 16778)
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
-- TOC entry 181 (class 1259 OID 16782)
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
-- TOC entry 182 (class 1259 OID 16784)
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

insert into logins (login,senha,nivel,nome) values ('admin','21232f297a57a5a743894a0e4a801fc3',2,'Admin');


ALTER TABLE public.salas OWNER TO postgres;

--
-- TOC entry 2071 (class 0 OID 0)
-- Dependencies: 182
-- Name: COLUMN salas.direito; Type: COMMENT; Schema: public; Owner: postgres
--

COMMENT ON COLUMN salas.direito IS 'a - para alunos e prof | p - para prof somente';


--
-- TOC entry 183 (class 1259 OID 16788)
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
-- TOC entry 184 (class 1259 OID 16790)
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
-- TOC entry 185 (class 1259 OID 16794)
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
-- TOC entry 2072 (class 0 OID 0)
-- Dependencies: 185
-- Name: COLUMN usuarios.tipo; Type: COMMENT; Schema: public; Owner: postgres
--

COMMENT ON COLUMN usuarios.tipo IS 'a - para alunos| p - para prof somente';


--
-- TOC entry 2065 (class 0 OID 0)
-- Dependencies: 7
-- Name: public; Type: ACL; Schema: -; Owner: postgres
--

REVOKE ALL ON SCHEMA public FROM PUBLIC;
REVOKE ALL ON SCHEMA public FROM postgres;
GRANT ALL ON SCHEMA public TO postgres;
GRANT ALL ON SCHEMA public TO PUBLIC;


-- Completed on 2016-04-15 08:15:14 BRT

--
-- PostgreSQL database dump complete
--

