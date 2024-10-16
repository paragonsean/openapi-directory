/**
 * App Center Client
 * Microsoft Visual Studio App Center API
 *
 * The version of the OpenAPI document: v0.1
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAISymbolUploadUserInfo.h
 *
 * 
 */

#ifndef OAISymbolUploadUserInfo_H
#define OAISymbolUploadUserInfo_H

#include <QJsonObject>

#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAISymbolUploadUserInfo : public OAIObject {
public:
    OAISymbolUploadUserInfo();
    OAISymbolUploadUserInfo(QString json);
    ~OAISymbolUploadUserInfo() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getDisplayName() const;
    void setDisplayName(const QString &display_name);
    bool is_display_name_Set() const;
    bool is_display_name_Valid() const;

    QString getEmail() const;
    void setEmail(const QString &email);
    bool is_email_Set() const;
    bool is_email_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_display_name;
    bool m_display_name_isSet;
    bool m_display_name_isValid;

    QString m_email;
    bool m_email_isSet;
    bool m_email_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAISymbolUploadUserInfo)

#endif // OAISymbolUploadUserInfo_H
