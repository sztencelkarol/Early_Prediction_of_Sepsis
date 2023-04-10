from preprocessing.Preprocessor import Preprocessor


if __name__ == "__main__":
    path_vital = "data/vital.csv"
    path_similar = "data/similar.json"
    path_grp_index = "data/group_index_dict.json"
    savePath = "generated_data"
    prep = Preprocessor(path_vital, path_grp_index, path_similar)
    #if you dont pass savePAth json wont be generated but the memeber variable
    #list will be and it will be accessible for testing. 
    prep.gen_index_feature_list(savePath)
    prep.gen_index_group_dict(savePath)
    prep.gen_feature_index_dict(savePath)
    prep.gen_patient_time_dict(savePath)

    prep.gen_feature_value_order_dict(savePath)
    prep.gen_patient_time_record_dict(savePath)

