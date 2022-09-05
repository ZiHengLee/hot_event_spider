import json,requests

def save(filename, content):
    ''' 写文件
    Args:
        filename: str, 文件路径
        content: str/dict, 需要写入的内容
    Returns:
        None
    '''
    with open(filename, 'w', encoding='utf-8') as f:
        # 写 JSON
        if filename.endswith('.json') and isinstance(content, dict):
            json.dump(content, f, ensure_ascii=False, indent=2)
        # 其他
        else:
            f.write(content)


def load(filename):
    ''' 读文件
    Args:
        filename: str, 文件路径
    Returns:
        文件所有内容 字符串
    '''
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
        return content
    return

def sync_call_dingding(url, content, at_mobiles=None):
    header = {
        "Content-Type": "application/json",
        "Charset": "UTF-8"
    }
    if len(content) > 4096:
        content = content[:4096]
    msg = {
        "msgtype": "text",
        "text": {
            "content": content
        },
        "at": {
            "atMobiles": at_mobiles,
            "isAtAll": False
        }
    }
    data = json.dumps(msg)
    ret = requests.post(url=url, data=data, headers=header)
    print('sync_call_dingding ret status: %s, text: %s' % (ret.status_code, ret.text))
    return