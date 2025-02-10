import os

def set_proxy(proxy_host="127.0.0.1", proxy_port="7890"):
    """
    设置全局代理
    :param proxy_host: 代理服务器地址，默认为本地
    :param proxy_port: 代理服务器端口，默认为clash的7890端口
    """
    proxy_url = f"http://{proxy_host}:{proxy_port}"
    os.environ["http_proxy"] = proxy_url
    os.environ["https_proxy"] = proxy_url
    
def unset_proxy():
    """
    取消全局代理设置
    """
    if "http_proxy" in os.environ:
        del os.environ["http_proxy"]
    if "https_proxy" in os.environ:
        del os.environ["https_proxy"] 