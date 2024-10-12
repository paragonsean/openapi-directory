/**
 * BBC Nitro API
 * BBC Nitro is the BBC's application programming interface (API) for BBC Programmes Metadata.
 *
 * The version of the OpenAPI document: 1.0.0
 * Contact: nitro@bbc.co.uk
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIErrorModel_fault_detail.h
 *
 * 
 */

#ifndef OAIErrorModel_fault_detail_H
#define OAIErrorModel_fault_detail_H

#include <QJsonObject>

#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIErrorModel_fault_detail : public OAIObject {
public:
    OAIErrorModel_fault_detail();
    OAIErrorModel_fault_detail(QString json);
    ~OAIErrorModel_fault_detail() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getErrorcode() const;
    void setErrorcode(const QString &errorcode);
    bool is_errorcode_Set() const;
    bool is_errorcode_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_errorcode;
    bool m_errorcode_isSet;
    bool m_errorcode_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIErrorModel_fault_detail)

#endif // OAIErrorModel_fault_detail_H
