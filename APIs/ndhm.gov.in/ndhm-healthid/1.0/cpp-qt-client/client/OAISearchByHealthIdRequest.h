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
 * OAISearchByHealthIdRequest.h
 *
 * 
 */

#ifndef OAISearchByHealthIdRequest_H
#define OAISearchByHealthIdRequest_H

#include <QJsonObject>

#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAISearchByHealthIdRequest : public OAIObject {
public:
    OAISearchByHealthIdRequest();
    OAISearchByHealthIdRequest(QString json);
    ~OAISearchByHealthIdRequest() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getHealthId() const;
    void setHealthId(const QString &health_id);
    bool is_health_id_Set() const;
    bool is_health_id_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_health_id;
    bool m_health_id_isSet;
    bool m_health_id_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAISearchByHealthIdRequest)

#endif // OAISearchByHealthIdRequest_H
