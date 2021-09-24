import pickle
def prediction_model(qty_slash_url,qty_equal_url,length_url,qty_dot_domain,directory_length,qty_hyphen_params,qty_percent_params,asn_ip,time_domain_activation,ttl_hostname):
    x=[[qty_slash_url,qty_equal_url,length_url,qty_dot_domain,directory_length,qty_hyphen_params,qty_percent_params,asn_ip,time_domain_activation,ttl_hostname]]
    classifier=pickle.load(open('classifier.pkl','rb'))
    prediction=classifier.predict(x)

    if prediction==1:
        return "This is the Phishing url please be safe Take Care."
    else:
        return "Hi Welcome ,This is not a phishing URL ,be Happy"
    return prediction




