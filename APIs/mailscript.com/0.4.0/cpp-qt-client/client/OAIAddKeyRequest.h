/**
 * Mailscript
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 0.4.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIAddKeyRequest.h
 *
 * 
 */

#ifndef OAIAddKeyRequest_H
#define OAIAddKeyRequest_H

#include <QJsonObject>

#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIAddKeyRequest : public OAIObject {
public:
    OAIAddKeyRequest();
    OAIAddKeyRequest(QString json);
    ~OAIAddKeyRequest() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getName() const;
    void setName(const QString &name);
    bool is_name_Set() const;
    bool is_name_Valid() const;

    bool isRead() const;
    void setRead(const bool &read);
    bool is_read_Set() const;
    bool is_read_Valid() const;

    bool isWrite() const;
    void setWrite(const bool &write);
    bool is_write_Set() const;
    bool is_write_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_name;
    bool m_name_isSet;
    bool m_name_isValid;

    bool m_read;
    bool m_read_isSet;
    bool m_read_isValid;

    bool m_write;
    bool m_write_isSet;
    bool m_write_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIAddKeyRequest)

#endif // OAIAddKeyRequest_H
