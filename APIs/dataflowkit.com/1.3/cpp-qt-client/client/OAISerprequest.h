/**
 * Dataflow Kit Web Scraper
 * Render Javascript driven pages, while we internally manage Headless Chrome and proxies for you.   - Build a custom web scraper with our Visual point-and-click toolkit. - Scrape the most popular Search engines result pages (SERP). - Convert web pages to PDF and capture screenshots. *** ### Authentication Dataflow Kit API require you to sign up for an API key in order to use the API.   The API key can be found in the [DFK Dashboard](https://account.dataflowkit.com) after _free registration_.  Pass a secret API Key to all API requests to the server as the `api_key` query parameter.  
 *
 * The version of the OpenAPI document: 1.3
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAISerprequest.h
 *
 * 
 */

#ifndef OAISerprequest_H
#define OAISerprequest_H

#include <QJsonObject>

#include "OAIField.h"
#include <QList>
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIField;

class OAISerprequest : public OAIObject {
public:
    OAISerprequest();
    OAISerprequest(QString json);
    ~OAISerprequest() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QList<OAIField> getFields() const;
    void setFields(const QList<OAIField> &fields);
    bool is_fields_Set() const;
    bool is_fields_Valid() const;

    QString getFormat() const;
    void setFormat(const QString &format);
    bool is_format_Set() const;
    bool is_format_Valid() const;

    QString getName() const;
    void setName(const QString &name);
    bool is_name_Set() const;
    bool is_name_Valid() const;

    qint32 getPageNum() const;
    void setPageNum(const qint32 &page_num);
    bool is_page_num_Set() const;
    bool is_page_num_Valid() const;

    QString getProxy() const;
    void setProxy(const QString &proxy);
    bool is_proxy_Set() const;
    bool is_proxy_Valid() const;

    QString getType() const;
    void setType(const QString &type);
    bool is_type_Set() const;
    bool is_type_Valid() const;

    QString getUrl() const;
    void setUrl(const QString &url);
    bool is_url_Set() const;
    bool is_url_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QList<OAIField> m_fields;
    bool m_fields_isSet;
    bool m_fields_isValid;

    QString m_format;
    bool m_format_isSet;
    bool m_format_isValid;

    QString m_name;
    bool m_name_isSet;
    bool m_name_isValid;

    qint32 m_page_num;
    bool m_page_num_isSet;
    bool m_page_num_isValid;

    QString m_proxy;
    bool m_proxy_isSet;
    bool m_proxy_isValid;

    QString m_type;
    bool m_type_isSet;
    bool m_type_isValid;

    QString m_url;
    bool m_url_isSet;
    bool m_url_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAISerprequest)

#endif // OAISerprequest_H
