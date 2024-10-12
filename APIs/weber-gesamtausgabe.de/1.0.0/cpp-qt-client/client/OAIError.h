/**
 * WeGA API
 * ⚠️<b>DEPRECATION WARNING</b>⚠️<br/>This version of the WeGA API specification is outdated and superseded by [version 1.1.0](https://weber-gesamtausgabe.de/api/v1/openapi.json).  <br/> <br/> For feedback or requests about this API please contact stadler@weber-gesamtausgabe.de or start the discussion at https://github.com/Edirom/WeGA-WebApp
 *
 * The version of the OpenAPI document: 1.0.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIError.h
 *
 * 
 */

#ifndef OAIError_H
#define OAIError_H

#include <QJsonObject>

#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIError : public OAIObject {
public:
    OAIError();
    OAIError(QString json);
    ~OAIError() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    qint32 getCode() const;
    void setCode(const qint32 &code);
    bool is_code_Set() const;
    bool is_code_Valid() const;

    QString getFields() const;
    void setFields(const QString &fields);
    bool is_fields_Set() const;
    bool is_fields_Valid() const;

    QString getMessage() const;
    void setMessage(const QString &message);
    bool is_message_Set() const;
    bool is_message_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    qint32 m_code;
    bool m_code_isSet;
    bool m_code_isValid;

    QString m_fields;
    bool m_fields_isSet;
    bool m_fields_isValid;

    QString m_message;
    bool m_message_isSet;
    bool m_message_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIError)

#endif // OAIError_H
