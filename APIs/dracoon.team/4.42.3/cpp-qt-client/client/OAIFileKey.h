/**
 * DRACOON API
 * REST Web Services for DRACOON<br><br>This page provides an overview of all available and documented DRACOON APIs, which are grouped by tags.<br>Each tag provides a collection of APIs that are intended for a specific area of the DRACOON.<br><br><a title='Developer Information' href='https://developer.dracoon.com'>Developer Information</a>&emsp;&emsp;<a title='Get SDKs on GitHub' href='https://github.com/dracoon'>Get SDKs on GitHub</a><br><br><a title='Terms of service' href='https://www.dracoon.com/terms/general-terms-and-conditions/'>Terms of service</a>
 *
 * The version of the OpenAPI document: 4.42.3
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIFileKey.h
 *
 * File key information
 */

#ifndef OAIFileKey_H
#define OAIFileKey_H

#include <QJsonObject>

#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIFileKey : public OAIObject {
public:
    OAIFileKey();
    OAIFileKey(QString json);
    ~OAIFileKey() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getIv() const;
    void setIv(const QString &iv);
    bool is_iv_Set() const;
    bool is_iv_Valid() const;

    QString getKey() const;
    void setKey(const QString &key);
    bool is_key_Set() const;
    bool is_key_Valid() const;

    QString getTag() const;
    void setTag(const QString &tag);
    bool is_tag_Set() const;
    bool is_tag_Valid() const;

    QString getVersion() const;
    void setVersion(const QString &version);
    bool is_version_Set() const;
    bool is_version_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_iv;
    bool m_iv_isSet;
    bool m_iv_isValid;

    QString m_key;
    bool m_key_isSet;
    bool m_key_isValid;

    QString m_tag;
    bool m_tag_isSet;
    bool m_tag_isValid;

    QString m_version;
    bool m_version_isSet;
    bool m_version_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIFileKey)

#endif // OAIFileKey_H
