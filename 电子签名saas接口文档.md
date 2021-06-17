# README
------
  
## API目录
  
|  API名称 |  接口分组  |  可见性  |  认证方式  |  描述  |
|  ------- |  -------  |  -------  |  -------  |  -------  |
|  [pdfToPic](#0)  |  fr_tool_saas  |  PRIVATE  |  APP  |  存储临时PDF文件  |   
|  [addOrgInfo](#1)  |  fr_signature_saas  |  PRIVATE  |  APP  |  添加机构信息-管理  |   
|  [toPdfStat](#2)  |  fr_signature_saas  |  PRIVATE  |  APP  |  添加转pdf记录  |   
|  [getAllFileList](#3)  |  fr_signature_saas  |  PRIVATE  |  APPOPENID  |  获取任务中所有文件  |   
|  [getAllFileList](#3)  |  fr_signature_third_saas  |  PRIVATE  |  APP  |  获取任务中所有文件  |   
|  [ossCallback](#4)  |  fr_signature_saas  |  public  |    |  OSS好传回调  |   
|  [getUploadToken](#5)  |  fr_signature_saas  |  PRIVATE  |  APPOPENID  |  获取上传token  |   
|  [letterTemplate](#6)  |  fr_signature_saas  |  PRIVATE  |    |  html文件模板  |   
|  [getFileList](#7)  |  fr_signature_saas  |  PRIVATE  |  APPOPENID  |  小程序待签名文件列表  |   
|  [checkTaskInfo](#8)  |  fr_signature_saas  |  PRIVATE  |  APPOPENID  |  查看任务详情  |   
|  [checkTaskInfo](#8)  |  fr_signature_third_saas  |  PRIVATE  |  APP  |  查看任务详情  |   
|  [getOrgSealList](#9)  |  fr_signature_saas  |  PRIVATE  |  APPOPENID  |  获取机构所有的可用章  |   
|  [getQRCode](#10)  |  fr_signature_saas  |  PRIVATE  |  APP  |  获取二维码链接  |   
|  [createTask](#11)  |  fr_signature_saas  |  PRIVATE  |  APPOPENID  |  创建任务  |   
|  [createTask](#11)  |  fr_signature_third_saas  |  PRIVATE  |  APP  |  第三方创建任务  |   
|  [saveTempFile](#12)  |  fr_signature_saas  |  PRIVATE  |  APPOPENID  |  存储临时PDF文件  |   
|  [checkWillAuth](#13)  |  fr_signature_saas  |  PRIVATE  |  APPOPENID  |  校验意愿认证  |   
|  [getAllPersonForOrg](#14)  |  fr_signature_saas  |  PRIVATE  |  APPOPENID  |  获取所有机构和人员列表  |   
|  [getTempFile](#15)  |  fr_signature_saas  |  PRIVATE  |  APPOPENID  |  获取临时任务信息  |   
|  [deleteTaskInfo](#16)  |  fr_signature_saas  |  PRIVATE  |  APPOPENID  |  删除任务  |   
|  [getSignerList](#17)  |  fr_signature_saas  |  PRIVATE  |  APPOPENID  |  获取签名者列表  |   
|  [getTaskList](#18)  |  fr_signature_saas  |  PRIVATE  |  APPOPENID  |  获取用户任务列表  |   
|  [getTaskList](#18)  |  fr_signature_third_saas  |  PRIVATE  |  APP  |  获取任务列表  |   
|  [getScanSignStatus](#19)  |  fr_signature_saas  |  PRIVATE  |  APPOPENID  |  获取扫二维码签名状态  |   
|  [getElectronicSealList](#25)  |  fr_signature_saas  |  PRIVATE  |  APP  |  获取机构下的签章列表-管理  |   
|  [getDataStat](#26)  |  fr_signature_saas  |  PRIVATE  |  APP  |  获取统计结果-管理  |   
|  [modifyUserInfo](#27)  |  fr_signature_saas  |  PRIVATE  |  APP  |  修改用户-管理  |   
|  [createUserInfo](#28)  |  fr_signature_saas  |  PRIVATE  |  APP  |  创建用户信息-管理  |   
|  [getOrgList](#29)  |  fr_signature_saas  |  PRIVATE  |  APP  |  获取机构列表-管理  |   
|  [addElectronicSeal](#30)  |  fr_signature_saas  |  PRIVATE  |  APP  |  添加电子签章-管理  |   
|  [addOrgInfo](#31)  |  fr_signature_saas  |  PRIVATE  |  APP  |  添加机构信息-管理  |   
|  [modifyElectronicSeal](#32)  |  fr_signature_saas  |  PRIVATE  |  APP  |  修改电子签章-管理  |   
|  [modifyOrgInfo](#33)  |  fr_signature_saas  |  PRIVATE  |  APP  |  修改机构-管理  |   
|  [getUserList](#34)  |  fr_signature_saas  |  PRIVATE  |  APP  |  获取用户信息-管理  |   
|  [uploadSignature](#36)  |  fr_signature_saas  |  PRIVATE  |  APPOPENID  |  上传签章  |   
|  [signFile](#37)  |  fr_signature_saas  |  PRIVATE  |  APPOPENID  |  确认签名  |   
|  [directSign](#38)  |  fr_signature_saas  |  PRIVATE  |  APP  |  直接签名  |   
|  [previewSign](#39)  |  fr_signature_saas  |  PRIVATE  |  APPOPENID  |  预览签名  |   
|  [refreshToken](#40)  |  fr_signature_saas  |  PRIVATE  |  APPOPENID  |  重新获取token  |   
|  [verifyUserInfo](#41)  |  fr_signature_saas  |  PRIVATE  |  OPENID  |  获取用户信息和token  |   
|  [verifyUserInfo](#41)  |  fr_signature_third_saas  |  PRIVATE  |  OPENID  |  获取用户信息和token  |   
|  [getOrgListForPhone](#42)  |  fr_signature_saas  |  PRIVATE  |  APP  |  通过手机号获取机构列表  |   
|  [getUserStat](#43)  |  fr_signature_saas  |  PRIVATE  |  APP  |  h5获取用户信息  |   
|  [getUserInfo](#44)  |  fr_signature_saas  |  PRIVATE  |  APP  |  h5获取用户信息  |   
|  [getVerificationCode](#45)  |  fr_signature_saas  |  PRIVATE  |  APP  |  获取验证码  |   
|  [sendMessage](#46)  |  fr_signature_saas  |  PRIVATE  |  APPOPENID  |  发送短息  |   
|  [getFindHtmlSubmit](#47)  |  fr_signature_saas  |  PRIVATE  |  APP  |  查找该模板的提交记录  |   
|  [sendSms](#48)  |  fr_signature_saas  |  PRIVATE  |  APP  |  提交记录保存后发送通知短信  |   
|  [getFindHtmlId](#49)  |  fr_signature_saas  |  PRIVATE  |  APP  |  获取某个html模板  |   
|  [saveSubmitRecords](#50)  |  fr_signature_saas  |  PRIVATE  |  APP  |  保存提交记录  |   
|  [getFindOIdSubmit](#51)  |  fr_signature_saas  |  PRIVATE  |  APP  |  查找机构下的提交记录  |   
|  [deleteHtml](#52)  |  fr_signature_saas  |  PRIVATE  |  APP  |  删除html模板  |   
|  [removeHtml](#53)  |  fr_signature_saas  |  PRIVATE  |  APP  |  修改模板内容  |   
|  [createTemplate](#54)  |  fr_signature_saas  |  PRIVATE  |  APP  |  创建html模板  |   
|  [htmlToPDF](#55)  |  fr_signature_saas  |  PRIVATE  |  APP  |  将html模板中参数进行替换，将模板上传oss上，在将html转成pdf返回  |   
|  [findHtml](#56)  |  fr_signature_saas  |  PRIVATE  |    |  获取所有的html模板  |   
|  [verifyCode](#57)  |  fr_signature_saas  |  PRIVATE  |  APP  |  校验验证码  |   

### <span id=0>pdfToPic</span>
##### 请求方法：POST
##### 接口分组：fr_tool_saas
##### 可见性：PRIVATE
##### 接口备注：存储临时PDF文件
|  参数名  |  参数位置  |  参数类型  |  描述  |  是否必传  |
|  ------- |  -------  |  -------  |  -------  |  -------  |
 |  pdf_url  |  Body  |  String  |  token  |  是  |
|  page  |  Body  |  String  |  返回页数,超过即使最大  |    |
|  dpi  |  Body  |  String  |  分辨率,像素数 可直接填写数字 例如 72 或者 100x100  |    |
|  width  |  Body  |  String  |  指定高 需配合 height 一起使用  |    |
|  height  |  Body  |  String  |  指定宽 需配合 width 一起使用  |    |
|  option_str  |  Body  |  String  |  gs命令 填写需保证正确性 主动覆盖以上所有参数  |    |

------


### <span id=1>addOrgInfo</span>
##### 请求方法：POST
##### 接口分组：fr_signature_saas
##### 可见性：PRIVATE
##### 接口备注：添加机构信息-管理
|  参数名  |  参数位置  |  参数类型  |  描述  |  是否必传  |
|  ------- |  -------  |  -------  |  -------  |  -------  |
 |  org_code  |  Body  |  String  |  机构代码  |  是  |
|  org_name  |  Body  |  String  |  机构名  |  是  |

------


### <span id=2>toPdfStat</span>
##### 请求方法：POST
##### 接口分组：fr_signature_saas
##### 可见性：PRIVATE
##### 接口备注：添加转pdf记录
|  参数名  |  参数位置  |  参数类型  |  描述  |  是否必传  |
|  ------- |  -------  |  -------  |  -------  |  -------  |
 |  token  |  Body  |  String  |  token  |  是  |
|  pic_number  |  Body  |  String  |  word文档数量  |    |
|  word_number  |  Body  |  String  |  图片数量  |    |
|  html_number  |  Body  |  String  |  html数量  |    |

------


### <span id=3>getAllFileList</span>
##### 请求方法：GET
##### 接口分组：fr_signature_saas
##### 可见性：PRIVATE
##### 接口备注：获取任务中所有文件
|  参数名  |  参数位置  |  参数类型  |  描述  |  是否必传  |
|  ------- |  -------  |  -------  |  -------  |  -------  |
 |  token  |  query  |  String  |  token  |  是  |
|  tid  |  Query  |  String  |  任务id  |  是  |

------


### <span id=3>getAllFileList</span>
##### 请求方法：GET
##### 接口分组：fr_signature_third_saas
##### 可见性：PRIVATE
##### 接口备注：获取任务中所有文件
|  参数名  |  参数位置  |  参数类型  |  描述  |  是否必传  |
|  ------- |  -------  |  -------  |  -------  |  -------  |
 |  tid  |  Query  |  String  |  任务id  |  是  |

------


### <span id=4>ossCallback</span>
##### 请求方法：POST
##### 接口分组：fr_signature_saas
##### 可见性：public
##### 接口备注：OSS好传回调
|  参数名  |  参数位置  |  参数类型  |  描述  |  是否必传  |
|  ------- |  -------  |  -------  |  -------  |  -------  |
 
------


### <span id=5>getUploadToken</span>
##### 请求方法：GET
##### 接口分组：fr_signature_saas
##### 可见性：PRIVATE
##### 接口备注：获取上传token
|  参数名  |  参数位置  |  参数类型  |  描述  |  是否必传  |
|  ------- |  -------  |  -------  |  -------  |  -------  |
 |  token  |  query  |  String  |  token  |  是  |
|  dir  |  Query  |  String  |  文件位置  |  是  |

------


### <span id=6>letterTemplate</span>
##### 请求方法：POST
##### 接口分组：fr_signature_saas
##### 可见性：PRIVATE
##### 接口备注：html文件模板
|  参数名  |  参数位置  |  参数类型  |  描述  |  是否必传  |
|  ------- |  -------  |  -------  |  -------  |  -------  |
 |  action  |  Body  |  String  |  操作 ADD/GET/DEL/GETALL  |  是  |
|  oid  |  Body  |  String  |  机构名称  |    |
|  type  |  Body  |  String  |  类型  |    |
|  lt_name  |  Body  |  String  |  模板名称  |    |
|  lt_id  |  Body  |  String  |  模板id  |    |
|  data  |  Body  |  String  |  模板内容  |    |
|  params  |  Body  |  String  |  模板参数  |    |

------


### <span id=7>getFileList</span>
##### 请求方法：GET
##### 接口分组：fr_signature_saas
##### 可见性：PRIVATE
##### 接口备注：小程序待签名文件列表
|  参数名  |  参数位置  |  参数类型  |  描述  |  是否必传  |
|  ------- |  -------  |  -------  |  -------  |  -------  |
 |  token  |  query  |  String  |  token  |  是  |
|  tid  |  Query  |  String  |  任务id  |  是  |
|  did_list  |  Query  |  String  |  任务列表  |  是  |

------


### <span id=8>checkTaskInfo</span>
##### 请求方法：POST
##### 接口分组：fr_signature_saas
##### 可见性：PRIVATE
##### 接口备注：查看任务详情
|  参数名  |  参数位置  |  参数类型  |  描述  |  是否必传  |
|  ------- |  -------  |  -------  |  -------  |  -------  |
 |  token  |  Body  |  String  |  token  |  是  |
|  tid  |  Body  |  String  |  用户id  |  是  |

------


### <span id=8>checkTaskInfo</span>
##### 请求方法：POST
##### 接口分组：fr_signature_third_saas
##### 可见性：PRIVATE
##### 接口备注：查看任务详情
|  参数名  |  参数位置  |  参数类型  |  描述  |  是否必传  |
|  ------- |  -------  |  -------  |  -------  |  -------  |
 |  tid  |  Body  |  String  |  用户id  |  是  |

------


### <span id=9>getOrgSealList</span>
##### 请求方法：GET
##### 接口分组：fr_signature_saas
##### 可见性：PRIVATE
##### 接口备注：获取机构所有的可用章
|  参数名  |  参数位置  |  参数类型  |  描述  |  是否必传  |
|  ------- |  -------  |  -------  |  -------  |  -------  |
 |  token  |  Query  |  String  |  token  |  是  |
|  oId  |  Query  |  String  |  企业id  |  是  |

------


### <span id=10>getQRCode</span>
##### 请求方法：GET
##### 接口分组：fr_signature_saas
##### 可见性：PRIVATE
##### 接口备注：获取二维码链接
|  参数名  |  参数位置  |  参数类型  |  描述  |  是否必传  |
|  ------- |  -------  |  -------  |  -------  |  -------  |
 |  data  |  Query  |  String  |  二维码参数  |  是  |

------


### <span id=11>createTask</span>
##### 请求方法：POST
##### 接口分组：fr_signature_saas
##### 可见性：PRIVATE
##### 接口备注：创建任务
|  参数名  |  参数位置  |  参数类型  |  描述  |  是否必传  |
|  ------- |  -------  |  -------  |  -------  |  -------  |
 |  token  |  Body  |  String  |  token  |  是  |
|  tmp_tid  |  Body  |  String  |  任务id  |    |
|  uid  |  Body  |  String  |  用户id  |  是  |
|  name  |  Body  |  String  |  任务名称  |  是  |
|  pdf_list  |  Body  |  String  |  文件具体签字信息  |  是  |
|  signature_type  |  Body  |  String  |  签章类型  |  是  |
|  auth_type  |  Body  |  String  |  身份验证方式  |  是  |
|  will_auth  |  Body  |  String  |  意愿认证  |    |
|  sign_end_time  |  Body  |  String  |  签署过期时间  |  是  |
|  person_list  |  Body  |  String  |  签名人列表  |  是  |
|  CaClientIp  |  Body  |  String  |  ip  |    |

------


### <span id=11>createTask</span>
##### 请求方法：POST
##### 接口分组：fr_signature_third_saas
##### 可见性：PRIVATE
##### 接口备注：第三方创建任务
|  参数名  |  参数位置  |  参数类型  |  描述  |  是否必传  |
|  ------- |  -------  |  -------  |  -------  |  -------  |
 |  oId  |  Body  |  String  |  机构id  |  是  |
|  name  |  Body  |  String  |  任务名称  |  是  |
|  pdf_list  |  Body  |  String  |  文件具体签字信息  |  是  |
|  person_list  |  Body  |  String  |  签名人列表  |  是  |
|  type  |  Body  |  String  |  操作类型  |    |
|  uid  |  Body  |  String  |  用户id  |    |
|  signature_type  |  Body  |  String  |  签章类型  |    |
|  auth_type  |  Body  |  String  |  身份验证方式  |    |
|  will_auth  |  Body  |  String  |  意愿认证  |    |
|  sign_end_time  |  Body  |  String  |  签署过期时间  |    |
|  CaClientIp  |  Body  |  String  |  ip  |    |

------


### <span id=12>saveTempFile</span>
##### 请求方法：POST
##### 接口分组：fr_signature_saas
##### 可见性：PRIVATE
##### 接口备注：存储临时PDF文件
|  参数名  |  参数位置  |  参数类型  |  描述  |  是否必传  |
|  ------- |  -------  |  -------  |  -------  |  -------  |
 |  token  |  Body  |  String  |  token  |  是  |
|  uid  |  Body  |  String  |  用户id  |  是  |
|  tmp_tid  |  Body  |  String  |  临时任务id  |    |
|  name  |  Body  |  String  |  任务名  |  是  |
|  pdf_list  |  Body  |  String  |  pdf文件列表   [ { file_name, url } .... ]   |  是  |
|  signature_type  |  Body  |  String  |  签章类型  |    |
|  auth_type  |  Body  |  String  |  身份验证方式  |    |
|  sign_end_time  |  Body  |  String  |  签署过期时间  |    |
|  will_auth  |  Body  |  String  |  意愿认证  |    |

------


### <span id=13>checkWillAuth</span>
##### 请求方法：POST
##### 接口分组：fr_signature_saas
##### 可见性：PRIVATE
##### 接口备注：校验意愿认证
|  参数名  |  参数位置  |  参数类型  |  描述  |  是否必传  |
|  ------- |  -------  |  -------  |  -------  |  -------  |
 |  token  |  Body  |  String  |  token  |  是  |
|  will_auth  |  Body  |  String  |  意愿认证  |  是  |
|  code  |  Body  |  String  |  验证码  |    |

------


### <span id=14>getAllPersonForOrg</span>
##### 请求方法：GET
##### 接口分组：fr_signature_saas
##### 可见性：PRIVATE
##### 接口备注：获取所有机构和人员列表
|  参数名  |  参数位置  |  参数类型  |  描述  |  是否必传  |
|  ------- |  -------  |  -------  |  -------  |  -------  |
 |  token  |  Query  |  String  |  token  |  是  |

------


### <span id=15>getTempFile</span>
##### 请求方法：GET
##### 接口分组：fr_signature_saas
##### 可见性：PRIVATE
##### 接口备注：获取临时任务信息
|  参数名  |  参数位置  |  参数类型  |  描述  |  是否必传  |
|  ------- |  -------  |  -------  |  -------  |  -------  |
 |  token  |  query  |  String  |  token  |  是  |
|  uid  |  query  |  String  |  用户id  |  是  |
|  tmp_tid  |  query  |  String  |  临时任务id  |    |

------


### <span id=16>deleteTaskInfo</span>
##### 请求方法：POST
##### 接口分组：fr_signature_saas
##### 可见性：PRIVATE
##### 接口备注：删除任务
|  参数名  |  参数位置  |  参数类型  |  描述  |  是否必传  |
|  ------- |  -------  |  -------  |  -------  |  -------  |
 |  token  |  Body  |  String  |  token  |  是  |
|  action  |  Body  |  String  |  任务id  |    |
|  tid  |  Body  |  String  |  任务id  |  是  |
|  uid  |  Body  |  String  |  用户id  |  是  |

------


### <span id=17>getSignerList</span>
##### 请求方法：GET
##### 接口分组：fr_signature_saas
##### 可见性：PRIVATE
##### 接口备注：获取签名者列表
|  参数名  |  参数位置  |  参数类型  |  描述  |  是否必传  |
|  ------- |  -------  |  -------  |  -------  |  -------  |
 |  token  |  Query  |  String  |  token  |  是  |
|  tid  |  Query  |  String  |  任务id  |  是  |

------


### <span id=18>getTaskList</span>
##### 请求方法：GET
##### 接口分组：fr_signature_saas
##### 可见性：PRIVATE
##### 接口备注：获取用户任务列表
|  参数名  |  参数位置  |  参数类型  |  描述  |  是否必传  |
|  ------- |  -------  |  -------  |  -------  |  -------  |
 |  token  |  query  |  String  |  token  |  是  |
|  uid  |  query  |  String  |  用户id  |  是  |
|  page  |  query  |  String  |  当前页  |    |
|  size  |  query  |  String  |  每页数量  |    |

------


### <span id=18>getTaskList</span>
##### 请求方法：GET
##### 接口分组：fr_signature_third_saas
##### 可见性：PRIVATE
##### 接口备注：获取任务列表
|  参数名  |  参数位置  |  参数类型  |  描述  |  是否必传  |
|  ------- |  -------  |  -------  |  -------  |  -------  |
 |  type  |  query  |  String  |  操作类型  |    |
|  oId  |  query  |  String  |  机构id  |  是  |
|  phone  |  query  |  String  |  手机号  |    |
|  uid  |  query  |  String  |  用户id  |    |
|  page  |  query  |  String  |  当前页  |    |
|  size  |  query  |  String  |  每页数量  |    |

------


### <span id=19>getScanSignStatus</span>
##### 请求方法：GET
##### 接口分组：fr_signature_saas
##### 可见性：PRIVATE
##### 接口备注：获取扫二维码签名状态
|  参数名  |  参数位置  |  参数类型  |  描述  |  是否必传  |
|  ------- |  -------  |  -------  |  -------  |  -------  |
 |  token  |  Query  |  String  |  token  |  是  |
|  scan_code  |  Query  |  String  |  扫码编号  |  是  |

------


### <span id=25>getElectronicSealList</span>
##### 请求方法：GET
##### 接口分组：fr_signature_saas
##### 可见性：PRIVATE
##### 接口备注：获取机构下的签章列表-管理
|  参数名  |  参数位置  |  参数类型  |  描述  |  是否必传  |
|  ------- |  -------  |  -------  |  -------  |  -------  |
 |  oId  |  Query  |  String  |  机构ID  |  是  |

------


### <span id=26>getDataStat</span>
##### 请求方法：GET
##### 接口分组：fr_signature_saas
##### 可见性：PRIVATE
##### 接口备注：获取统计结果-管理
|  参数名  |  参数位置  |  参数类型  |  描述  |  是否必传  |
|  ------- |  -------  |  -------  |  -------  |  -------  |
 |  oId  |  Query  |  String  |  机构id  |    |
|  start_time  |  Query  |  String  |  开始时间  |    |
|  end_time  |  Query  |  String  |  结束时间  |    |

------


### <span id=27>modifyUserInfo</span>
##### 请求方法：POST
##### 接口分组：fr_signature_saas
##### 可见性：PRIVATE
##### 接口备注：修改用户-管理
|  参数名  |  参数位置  |  参数类型  |  描述  |  是否必传  |
|  ------- |  -------  |  -------  |  -------  |  -------  |
 |  action  |  Body  |  String  |  update / delete 删除只需要 action 传 delete  |  是  |
|  uid  |  Body  |  String  |  用户id  |  是  |
|  cert_no  |  Body  |  String  |  身份证  |    |
|  phone  |  Body  |  String  |  手机号  |    |
|  name  |  Body  |  String  |  姓名  |    |
|  org_list  |  Body  |  String  |  机构列表  |    |
|  status  |  Body  |  String  |  状态  |    |

------


### <span id=28>createUserInfo</span>
##### 请求方法：POST
##### 接口分组：fr_signature_saas
##### 可见性：PRIVATE
##### 接口备注：创建用户信息-管理
|  参数名  |  参数位置  |  参数类型  |  描述  |  是否必传  |
|  ------- |  -------  |  -------  |  -------  |  -------  |
 |  phone  |  Body  |  String  |  手机号  |  是  |
|  name  |  Body  |  String  |  姓名  |    |
|  cert_no  |  Body  |  String  |  身份证  |    |
|  org_list  |  Body  |  String  |  机构列表  |  是  |
|  status  |  Body  |  String  |  状态  |    |

------


### <span id=29>getOrgList</span>
##### 请求方法：GET
##### 接口分组：fr_signature_saas
##### 可见性：PRIVATE
##### 接口备注：获取机构列表-管理
|  参数名  |  参数位置  |  参数类型  |  描述  |  是否必传  |
|  ------- |  -------  |  -------  |  -------  |  -------  |
 |  org_name  |  Query  |  String  |  机构名  |    |

------


### <span id=30>addElectronicSeal</span>
##### 请求方法：POST
##### 接口分组：fr_signature_saas
##### 可见性：PRIVATE
##### 接口备注：添加电子签章-管理
|  参数名  |  参数位置  |  参数类型  |  描述  |  是否必传  |
|  ------- |  -------  |  -------  |  -------  |  -------  |
 |  oId  |  Body  |  String  |  机构ID  |  是  |
|  e_name  |  Body  |  String  |  印章名  |  是  |
|  creator  |  Body  |  String  |  创建人  |  是  |
|  base64  |  Body  |  String  |  印章图片base64  |  是  |
|  type  |  Body  |  String  |  印章类型  |  是  |
|  status  |  Body  |  String  |  状态 1 弃用 -1 废弃  |    |
|  b_is_default  |  Body  |  String  |  状态 1 默认 -1 非默认  |    |
|  CaClientIp  |  Body  |  String  |  ip  |    |

------


### <span id=31>addOrgInfo</span>
##### 请求方法：POST
##### 接口分组：fr_signature_saas
##### 可见性：PRIVATE
##### 接口备注：添加机构信息-管理
|  参数名  |  参数位置  |  参数类型  |  描述  |  是否必传  |
|  ------- |  -------  |  -------  |  -------  |  -------  |
 |  org_code  |  Body  |  String  |  机构代码  |  是  |
|  org_name  |  Body  |  String  |  机构名  |  是  |

------


### <span id=32>modifyElectronicSeal</span>
##### 请求方法：POST
##### 接口分组：fr_signature_saas
##### 可见性：PRIVATE
##### 接口备注：修改电子签章-管理
|  参数名  |  参数位置  |  参数类型  |  描述  |  是否必传  |
|  ------- |  -------  |  -------  |  -------  |  -------  |
 |  eid  |  Body  |  String  |  印章id  |  是  |
|  status  |  Body  |  String  |  状态 1 弃用 -1 废弃  |    |
|  b_is_default  |  Body  |  String  |  状态 1 默认 -1 非默认  |    |

------


### <span id=33>modifyOrgInfo</span>
##### 请求方法：POST
##### 接口分组：fr_signature_saas
##### 可见性：PRIVATE
##### 接口备注：修改机构-管理
|  参数名  |  参数位置  |  参数类型  |  描述  |  是否必传  |
|  ------- |  -------  |  -------  |  -------  |  -------  |
 |  action  |  Body  |  String  |  update / delete(暂不可用)   |  是  |
|  oId  |  Body  |  String  |  机构id  |  是  |
|  org_name  |  Body  |  String  |  机构名  |    |
|  org_code  |  Body  |  String  |  机构代码  |    |

------


### <span id=34>getUserList</span>
##### 请求方法：GET
##### 接口分组：fr_signature_saas
##### 可见性：PRIVATE
##### 接口备注：获取用户信息-管理
|  参数名  |  参数位置  |  参数类型  |  描述  |  是否必传  |
|  ------- |  -------  |  -------  |  -------  |  -------  |
 |  name  |  Query  |  String  |  姓名  |    |

------


### <span id=36>uploadSignature</span>
##### 请求方法：POST
##### 接口分组：fr_signature_saas
##### 可见性：PRIVATE
##### 接口备注：上传签章
|  参数名  |  参数位置  |  参数类型  |  描述  |  是否必传  |
|  ------- |  -------  |  -------  |  -------  |  -------  |
 |  token  |  Body  |  String  |  token  |  是  |
|  signee_list  |  Body  |  String  |  签名数据 [ { did, signee_id } ]  |  是  |
|  signature_base64  |  Body  |  String  |  签名图片  |    |
|  signature_url  |  Body  |  String  |  签名图片url  |    |
|  name  |  Body  |  String  |  姓名  |    |
|  CaClientIp  |  Body  |  String  |  ip  |    |

------


### <span id=37>signFile</span>
##### 请求方法：POST
##### 接口分组：fr_signature_saas
##### 可见性：PRIVATE
##### 接口备注：确认签名
|  参数名  |  参数位置  |  参数类型  |  描述  |  是否必传  |
|  ------- |  -------  |  -------  |  -------  |  -------  |
 |  token  |  Body  |  String  |  token  |  是  |
|  sign_list  |  Body  |  String  |  签名数据 [ { did, signee_id, file_width, xy_data, signature_height } ]  |  是  |

------


### <span id=38>directSign</span>
##### 请求方法：POST
##### 接口分组：fr_signature_saas
##### 可见性：PRIVATE
##### 接口备注：直接签名
|  参数名  |  参数位置  |  参数类型  |  描述  |  是否必传  |
|  ------- |  -------  |  -------  |  -------  |  -------  |
 |  name  |  Body  |  String  |  签名人  |  是  |
|  phone  |  Body  |  String  |  签名人手机  |  是  |
|  cert_no  |  Body  |  String  |  签名人身份证  |    |
|  signature_base64  |  Body  |  String  |  签名图片BASE64  |    |
|  signature_url  |  Body  |  String  |  签名图片URL  |    |
|  file_url  |  Body  |  String  |  文件url  |  是  |
|  file_width  |  Body  |  String  |  文件宽度  |  是  |
|  file_name  |  Body  |  String  |  文件名  |    |
|  signature_height  |  Body  |  String  |  签名高度  |    |
|  xy_data  |  Body  |  String  |  签名位置信息 [{ x: 82.52, y: 235, page: 1 }]  |  是  |
|  CaClientIp  |  Body  |  String  |  ip  |    |

------


### <span id=39>previewSign</span>
##### 请求方法：POST
##### 接口分组：fr_signature_saas
##### 可见性：PRIVATE
##### 接口备注：预览签名
|  参数名  |  参数位置  |  参数类型  |  描述  |  是否必传  |
|  ------- |  -------  |  -------  |  -------  |  -------  |
 |  token  |  Body  |  String  |  token  |  是  |
|  sign_list  |  Body  |  String  |  签名数据 [ { did, signee_id, file_width, xy_data, signature_height } ]  |  是  |

------


### <span id=40>refreshToken</span>
##### 请求方法：POST
##### 接口分组：fr_signature_saas
##### 可见性：PRIVATE
##### 接口备注：重新获取token
|  参数名  |  参数位置  |  参数类型  |  描述  |  是否必传  |
|  ------- |  -------  |  -------  |  -------  |  -------  |
 |  token  |  Body  |  String  |  TOKEN  |  是  |

------


### <span id=41>verifyUserInfo</span>
##### 请求方法：POST
##### 接口分组：fr_signature_saas
##### 可见性：PRIVATE
##### 接口备注：获取用户信息和token
|  参数名  |  参数位置  |  参数类型  |  描述  |  是否必传  |
|  ------- |  -------  |  -------  |  -------  |  -------  |
 |  phone  |  Body  |  String  |  手机号  |  是  |
|  code  |  Body  |  String  |  验证码  |  是  |
|  oId  |  Body  |  String  |  机构id  |    |
|  scan_code  |  Body  |  String  |  扫码code  |    |
|  tid  |  Body  |  String  |  任务id  |    |
|  type  |  Body  |  String  |  操作模式  |    |

------


### <span id=41>verifyUserInfo</span>
##### 请求方法：POST
##### 接口分组：fr_signature_third_saas
##### 可见性：PRIVATE
##### 接口备注：获取用户信息和token
|  参数名  |  参数位置  |  参数类型  |  描述  |  是否必传  |
|  ------- |  -------  |  -------  |  -------  |  -------  |
 |  phone  |  Body  |  String  |  手机号  |  是  |
|  code  |  Body  |  String  |  验证码  |    |
|  oId  |  Body  |  String  |  机构id  |    |
|  scan_code  |  Body  |  String  |  扫码code  |    |
|  tid  |  Body  |  String  |  任务id  |    |
|  type  |  Body  |  String  |  操作模式  |  是  |

------


### <span id=42>getOrgListForPhone</span>
##### 请求方法：GET
##### 接口分组：fr_signature_saas
##### 可见性：PRIVATE
##### 接口备注：通过手机号获取机构列表
|  参数名  |  参数位置  |  参数类型  |  描述  |  是否必传  |
|  ------- |  -------  |  -------  |  -------  |  -------  |
 |  phone  |  Query  |  String  |  手机号  |  是  |

------


### <span id=43>getUserStat</span>
##### 请求方法：GET
##### 接口分组：fr_signature_saas
##### 可见性：PRIVATE
##### 接口备注：h5获取用户信息
|  参数名  |  参数位置  |  参数类型  |  描述  |  是否必传  |
|  ------- |  -------  |  -------  |  -------  |  -------  |
 |  token  |  Body  |  String  |  token  |  是  |
|  uid  |  Body  |  String  |  用户id  |  是  |

------


### <span id=44>getUserInfo</span>
##### 请求方法：GET
##### 接口分组：fr_signature_saas
##### 可见性：PRIVATE
##### 接口备注：h5获取用户信息
|  参数名  |  参数位置  |  参数类型  |  描述  |  是否必传  |
|  ------- |  -------  |  -------  |  -------  |  -------  |
 |  tid  |  Query  |  String  |  任务id  |  是  |
|  id_number  |  Query  |  String  |  id号码  |  是  |

------


### <span id=45>getVerificationCode</span>
##### 请求方法：GET
##### 接口分组：fr_signature_saas
##### 可见性：PRIVATE
##### 接口备注：获取验证码
|  参数名  |  参数位置  |  参数类型  |  描述  |  是否必传  |
|  ------- |  -------  |  -------  |  -------  |  -------  |
 |  phone  |  Query  |  String  |  手机号  |  是  |
|  action  |  Query  |  String  |  类型  |    |

------


### <span id=46>sendMessage</span>
##### 请求方法：POST
##### 接口分组：fr_signature_saas
##### 可见性：PRIVATE
##### 接口备注：发送短息
|  参数名  |  参数位置  |  参数类型  |  描述  |  是否必传  |
|  ------- |  -------  |  -------  |  -------  |  -------  |
 |  token  |  Body  |  String  |  token  |  是  |
|  tid  |  Body  |  String  |  手机号  |  是  |
|  ids  |  Body  |  String  |  签名人id列表  1,2,3,4  |  是  |

------


### <span id=47>getFindHtmlSubmit</span>
##### 请求方法：GET
##### 接口分组：fr_signature_saas
##### 可见性：PRIVATE
##### 接口备注：查找该模板的提交记录
|  参数名  |  参数位置  |  参数类型  |  描述  |  是否必传  |
|  ------- |  -------  |  -------  |  -------  |  -------  |
 |  html_id  |  Query  |  String  |  模板id  |  是  |

------


### <span id=48>sendSms</span>
##### 请求方法：GET
##### 接口分组：fr_signature_saas
##### 可见性：PRIVATE
##### 接口备注：提交记录保存后发送通知短信
|  参数名  |  参数位置  |  参数类型  |  描述  |  是否必传  |
|  ------- |  -------  |  -------  |  -------  |  -------  |
 |  url  |  Query  |  String  |  阿里云存取路径  |  是  |
|  phone  |  Query  |  String  |  电话号码  |  是  |

------


### <span id=49>getFindHtmlId</span>
##### 请求方法：GET
##### 接口分组：fr_signature_saas
##### 可见性：PRIVATE
##### 接口备注：获取某个html模板
|  参数名  |  参数位置  |  参数类型  |  描述  |  是否必传  |
|  ------- |  -------  |  -------  |  -------  |  -------  |
 |  html_id  |  Query  |  String  |  模板id  |  是  |

------


### <span id=50>saveSubmitRecords</span>
##### 请求方法：POST
##### 接口分组：fr_signature_saas
##### 可见性：PRIVATE
##### 接口备注：保存提交记录
|  参数名  |  参数位置  |  参数类型  |  描述  |  是否必传  |
|  ------- |  -------  |  -------  |  -------  |  -------  |
 |  html_id  |  Body  |  String  |  html模板id  |  是  |
|  org_code  |  Body  |  String  |  机构代码  |  是  |
|  name  |  Body  |  String  |  提交人姓名  |  是  |
|  phone  |  Body  |  String  |  提交人账号  |  是  |
|  signFile  |  Body  |  String  |  签名文件  |  是  |

------


### <span id=51>getFindOIdSubmit</span>
##### 请求方法：GET
##### 接口分组：fr_signature_saas
##### 可见性：PRIVATE
##### 接口备注：查找机构下的提交记录
|  参数名  |  参数位置  |  参数类型  |  描述  |  是否必传  |
|  ------- |  -------  |  -------  |  -------  |  -------  |
 |  oId  |  Query  |  String  |  机构id  |  是  |

------


### <span id=52>deleteHtml</span>
##### 请求方法：GET
##### 接口分组：fr_signature_saas
##### 可见性：PRIVATE
##### 接口备注：删除html模板
|  参数名  |  参数位置  |  参数类型  |  描述  |  是否必传  |
|  ------- |  -------  |  -------  |  -------  |  -------  |
 |  html_id  |  Query  |  String  |  模板id  |  是  |

------


### <span id=53>removeHtml</span>
##### 请求方法：POST
##### 接口分组：fr_signature_saas
##### 可见性：PRIVATE
##### 接口备注：修改模板内容
|  参数名  |  参数位置  |  参数类型  |  描述  |  是否必传  |
|  ------- |  -------  |  -------  |  -------  |  -------  |
 |  name  |  Body  |  String  |  模板名  |  是  |
|  htmlContent  |  Body  |  String  |  模板信息  |  是  |
|  parameterList  |  Body  |  String  |  模板中要替换的参数  |  是  |
|  oId  |  Body  |  String  |  项目类型  |  是  |
|  html_id  |  Body  |  String  |  模板的唯一id  |  是  |

------


### <span id=54>createTemplate</span>
##### 请求方法：POST
##### 接口分组：fr_signature_saas
##### 可见性：PRIVATE
##### 接口备注：创建html模板
|  参数名  |  参数位置  |  参数类型  |  描述  |  是否必传  |
|  ------- |  -------  |  -------  |  -------  |  -------  |
 |  name  |  Body  |  String  |  模板名  |  是  |
|  htmlContent  |  Body  |  String  |  模板信息  |  是  |
|  parameterList  |  Body  |  String  |  模板替换参数  |  是  |
|  oId  |  Body  |  String  |  项目类型  |  是  |

------


### <span id=55>htmlToPDF</span>
##### 请求方法：POST
##### 接口分组：fr_signature_saas
##### 可见性：PRIVATE
##### 接口备注：将html模板中参数进行替换，将模板上传oss上，在将html转成pdf返回
|  参数名  |  参数位置  |  参数类型  |  描述  |  是否必传  |
|  ------- |  -------  |  -------  |  -------  |  -------  |
 |  html_id  |  Body  |  String  |  html模板id  |  是  |
|  data  |  Body  |  String  |  要替换html模板中key和value  |  是  |

------


### <span id=56>findHtml</span>
##### 请求方法：GET
##### 接口分组：fr_signature_saas
##### 可见性：PRIVATE
##### 接口备注：获取所有的html模板
|  参数名  |  参数位置  |  参数类型  |  描述  |  是否必传  |
|  ------- |  -------  |  -------  |  -------  |  -------  |
 |  org_code  |  Query  |  String  |  机构代码  |  是  |

------


### <span id=57>verifyCode</span>
##### 请求方法：POST
##### 接口分组：fr_signature_saas
##### 可见性：PRIVATE
##### 接口备注：校验验证码
|  参数名  |  参数位置  |  参数类型  |  描述  |  是否必传  |
|  ------- |  -------  |  -------  |  -------  |  -------  |
 |  phone  |  Body  |  String  |  用户的电话号  |  是  |
|  code  |  Body  |  String  |  验证码  |  是  |

------

