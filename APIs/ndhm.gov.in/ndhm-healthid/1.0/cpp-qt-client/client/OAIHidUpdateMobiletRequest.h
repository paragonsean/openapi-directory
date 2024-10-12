/**
 * Health ID Service
 * It is important to standardize the process of identification of an individual across healthcare providers, to ensure that the created medical records are issued to the right individual or accessed by a Health Information User through appropriate consent.  In order to issue a Health ID to an individual, one only needs basic demographic details like Name, Year of Birth, Gender. In addition, citizens should be able to update contact information easily.
 *
 * The version of the OpenAPI document: 1.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIHidUpdateMobiletRequest.h
 *
 * 
 */

#ifndef OAIHidUpdateMobiletRequest_H
#define OAIHidUpdateMobiletRequest_H

#include <QJsonObject>

#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIHidUpdateMobiletRequest : public OAIObject {
public:
    OAIHidUpdateMobiletRequest();
    OAIHidUpdateMobiletRequest(QString json);
    ~OAIHidUpdateMobiletRequest() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getHealthIdNumber() const;
    void setHealthIdNumber(const QString &health_id_number);
    bool is_health_id_number_Set() const;
    bool is_health_id_number_Valid() const;

    QString getMobile() const;
    void setMobile(const QString &mobile);
    bool is_mobile_Set() const;
    bool is_mobile_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_health_id_number;
    bool m_health_id_number_isSet;
    bool m_health_id_number_isValid;

    QString m_mobile;
    bool m_mobile_isSet;
    bool m_mobile_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIHidUpdateMobiletRequest)

#endif // OAIHidUpdateMobiletRequest_H
