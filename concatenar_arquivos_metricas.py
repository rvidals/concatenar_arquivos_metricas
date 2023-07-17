import pandas as pd
import glob

class Concatena:
    """ 
    O objetivo dessa classe é concatenar os arquivos individuais das métricas geradas em R e exportadas em csv.
    """

    path = r'C:\Users\rogerio.siqueira\Documents\DEMANDAS_ROGERIO\RESTAURACAO_CERRADO\METRICAS_PAISAGEM\1-RESULTADOS\RECLASS\RIDE'

    def __init__(self) -> None:
        self.ano = input("Informe o ano: ")
        #Caso queira que seja interativo no TERMINAL
        self.metrica = input("Informe a métrica: p/c/l: ")
    def concat_tipo_metrica(self):
        self.metrica = metrica #Para ser interativo no TERMINAL, comentar essa linha!
        files = glob.glob(Concatena.path + f'/ride_lsm_{self.metrica}_*{self.ano}.csv')
        lista = []
        for i in range(len(files)):
            df = pd.read_csv(files[i])
            lista.append(df)

        df = pd.concat(lista)

        name = []
        type = []
        function_name = []
        if self.metrica.lower() == 'p':
            tipo = 'patch'
            for row in df['metric']:
                if row == 'area': 
                    name.append('patch area')
                    type.append('area and edge metric')
                    function_name.append('lsm_p_area')
                elif row == 'cai':
                    name.append('core area')
                    type.append('core area metric')
                    function_name.append('lsm_p_core')
                elif row == 'core':
                    name.append('patch area')
                    type.append('area and edge metric')
                    function_name.append('lsm_c_area_mn')
                elif row == 'enn':
                    name.append('euclidean nearest neighbor distance')
                    type.append('aggregation metric')
                    function_name.append('lsm_p_enn')
                elif row == 'ncore':
                    name.append('number of core areas')
                    type.append('core area metric')
                    function_name.append('lsm_p_ncore')
                else:
                    name.append('aggregation index')
                    type.append('aggregation metric')
                    function_name.append('lsm_c_ai')
        elif self.metrica.lower() == 'c':
            tipo = 'class'
            for row in df['metric']:
                if row == 'ai': 
                    name.append('aggregation index')
                    type.append('aggregation metric')
                    function_name.append('lsm_c_ai')
                elif row == 'area_cv':
                    name.append('patch area')
                    type.append('area and edge metric')
                    function_name.append('lsm_c_area_cv')
                elif row == 'area_mn':
                    name.append('patch area')
                    type.append('area and edge metric')
                    function_name.append('lsm_c_area_mn')
                elif row == 'area_sd':
                    name.append('patch area')
                    type.append('area and edge metric')
                    function_name.append('lsm_c_area_sd')
                elif row == 'ca':
                    name.append('total (class) area')
                    type.append('area and edge metric')
                    function_name.append('lsm_c_ca')
                elif row == 'core_cv':
                    name.append('core area index')
                    type.append('core area metric')
                    function_name.append('lsm_c_core_cv')
                elif row == 'core_mn':
                    name.append('core area index')
                    type.append('core area metric')
                    function_name.append('lsm_c_core_mn')
                elif row == 'core_sd':
                    name.append('core area index')
                    type.append('core area metric')
                    function_name.append('lsm_c_core_sd')
                elif row == 'iji':
                    name.append('interspersion and juxtaposition index')
                    type.append('aggregation metric')
                    function_name.append('lsm_c_iji')
                elif row == 'lpi':
                    name.append('largest patch index')
                    type.append('area and edge metric')
                    function_name.append('lsm_c_lpi')
                elif row == 'np':
                    name.append('number of patches')
                    type.append('aggregation metric')
                    function_name.append('lsm_c_np')
                elif row == 'pd':
                    name.append('patch density')
                    type.append('aggregation metric')
                    function_name.append('lsm_c_pd')
                elif row == 'pland':
                    name.append('percentage of landscape')
                    type.append('area and edge metric')
                    function_name.append('lsm_c_pland')
                elif row == 'tca':
                    name.append('total core area')
                    type.append('core area metric')
                    function_name.append('lsm_c_tca')
                elif row == 'ed':
                    name.append('edge density')
                    type.append('area and edge metric')
                    function_name.append('lsm_c_ed')
                elif row == 'enn_mn':
                    name.append('euclidean nearest neighbor distance')
                    type.append('aggregation metric')
                    function_name.append('lsm_c_enn_mn')
                else: 
                    name.append('core area percentage of landscape')
                    type.append('core area metric')
                    function_name.append('lsm_c_cpland')
        elif self.metrica.lower() == 'l':
            tipo = 'land'
            for row in df['metric']:
                if row == 'ai': 
                    name.append('aggregation index')
                    type.append('aggregation metric')
                    function_name.append('lsm_l_ai')
                elif row == 'area_cv':
                    name.append('patch area')
                    type.append('area and edge metric')
                    function_name.append('lsm_l_area_cv')
                elif row == 'area_mn':
                    name.append('patch area')
                    type.append('area and edge metric')
                    function_name.append('lsm_l_area_mn')
                elif row == 'area_sd':
                    name.append('patch area')
                    type.append('area and edge metric')
                    function_name.append('lsm_l_area_sd')
                elif row == 'cai_cv':
                    name.append('core area index')
                    type.append('core area metric')
                    function_name.append('lsm_l_cai_cv')
                elif row == 'cai_mn':
                    name.append('core area index')
                    type.append('core area metric')
                    function_name.append('lsm_l_cai_mn')
                elif row == 'cai_sd':
                    name.append('core area index')
                    type.append('core area metric')
                    function_name.append('lsm_l_cai_sd')
                elif row == 'lpi':
                    name.append('landscape shape index')
                    type.append('aggregation metric')
                    function_name.append('lsm_l_lsi')
                elif row == 'lsi':
                    name.append('patch area')
                    type.append('area and edge metric')
                    function_name.append('lsm_c_area_cv')
                elif row == 'mesh':
                    name.append('effective mesh size')
                    type.append('aggregation metric')
                    function_name.append('lsm_l_mesh')
                elif row == 'ndca':
                    name.append('number of disjunct core areas')
                    type.append('core area metric')
                    function_name.append('lsm_l_ndca')
                elif row == 'np':
                    name.append('number of patches')
                    type.append('aggregation metric')
                    function_name.append('lsm_l_np')
                elif row == 'para_cv':
                    name.append('perimeter-area ratio')
                    type.append('shape metric')
                    function_name.append('lsm_l_para_cv')
                elif row == 'para_mn':
                    name.append('perimeter-area ratio')
                    type.append('shape metric')
                    function_name.append('lsm_l_para_mn')
                elif row == 'para_sd':
                    name.append('perimeter-area ratio')
                    type.append('shape metric')
                    function_name.append('lsm_l_para_sd')
                else: 
                    name.append('patch density')
                    type.append('aggregation metric')
                    function_name.append('lsm_l_pd')
        df['name'] = name
        df['type'] = type
        df['function_name'] = function_name

        df = df.reset_index()
        try:
            df['index'] = df.index
        except:
            df.insert(0,'index',df.index)
        return df.to_csv( Concatena.path + f'/ride_lsm_{tipo}{self.ano}.csv', index=False)

if __name__ == '__main__':
    #Criar objeto concatenar
    concatenar =  Concatena()

    #Lista de métricas
    metricas = ['p','c','l']
    for metrica in metricas:
        concatenar.concat_tipo_metrica()
        concatenar.metrica = metrica