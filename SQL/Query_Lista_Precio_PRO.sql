Select ae.art_codigo_externo, p.porcentaje, p.vigencia, p.vigencia_hasta
 from porcentajes_articulos_ventas p, locales l, articulos_empresas ae
 where p.loc_lis_loc_codigo=l.codigo
 and p.art_codigo=ae.art_codigo
 and p.dim_con_numero = 0 
 and p.loc_lis_lis_pre_ve_codigo = :Lista_Precio
 and l.loc_cod_empresa = :Sucursal
 and p.emp_codigo = 1
 and p.porcentaje > 1
 and sysdate between p.vigencia and p.vigencia_hasta