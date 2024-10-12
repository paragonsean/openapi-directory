/**
 * Gateway
 * Gateway is the hub that routes/orchestrates the interaction between consent managers and API bridges. There are 5 categories of APIs; discovery, link, consent flow, data flow and  monitoring. To reflect the consumers of APIs, the above apis are also categorized under cm facing, hiu facing and hip facing  
 *
 * The version of the OpenAPI document: 0.5
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIPatientCareContextLinkResponse_acknowledgement.h
 *
 * 
 */

#ifndef OAIPatientCareContextLinkResponse_acknowledgement_H
#define OAIPatientCareContextLinkResponse_acknowledgement_H

#include <QJsonObject>

#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIPatientCareContextLinkResponse_acknowledgement : public OAIObject {
public:
    OAIPatientCareContextLinkResponse_acknowledgement();
    OAIPatientCareContextLinkResponse_acknowledgement(QString json);
    ~OAIPatientCareContextLinkResponse_acknowledgement() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getStatus() const;
    void setStatus(const QString &status);
    bool is_status_Set() const;
    bool is_status_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_status;
    bool m_status_isSet;
    bool m_status_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIPatientCareContextLinkResponse_acknowledgement)

#endif // OAIPatientCareContextLinkResponse_acknowledgement_H
