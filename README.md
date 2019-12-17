## 简介

函数计算无缝迁移 WSGI Application 示例

## 部署

### 准备工作

- 免费开通 [函数计算](https://statistics.functioncompute.com/?title=PythonWeb&theme=PythonWeb&author=rsong&src=article&url=http://fc.console.aliyun.com)

- 准备域名(国内的需要备案过)， 并将域名 CNAME 解析到对应的 FC EndPoint

> 比如将自己的域名域名 flask.mydomain.cn 解析到 123456.cn-hangzhou.fc.aliyuncs.com, 对应的域名、accountId 和 region 修改成自己的

### 安装 Fun 工具

-	安装版本为8.x 最新版或者10.x 、12.x [nodejs](https://nodejs.org/en/download/package-manager/#debian-and-ubuntu-based-linux-distributions-enterprise-linux-fedora-and-snap-packages)

-	安装 [funcraf](https://github.com/alibaba/funcraft/blob/master/docs/usage/installation-zh.md)

	```
	$ npm install @alicloud/fun -g
	```

- 安装完成后， 执行 `fun config`，按照提示完成 fun 的配置，参考：[getting_started](https://github.com/alibaba/funcraft/blob/master/docs/usage/getting_started-zh.md)

### Clone 工程，在工程目录上，命令行输入 `fun deploy` 执行

```
$ git clone https://github.com/awesome-fc/fc-python-web.git
$ cd fc-python-web
# 先将 template 中的 CustomDomain 修改成自己的
$ fun deploy
```