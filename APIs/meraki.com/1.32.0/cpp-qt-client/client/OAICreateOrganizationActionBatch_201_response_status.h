/**
 * Meraki Dashboard API
 * The Cisco Meraki Dashboard API is a modern REST API based on the OpenAPI specification.  > Date: 05 April, 2023 > > [Recent Updates](https://meraki.io/whats-new/)  ---  [API Documentation](https://meraki.io/api)  [Community Support](https://meraki.io/community)  [Meraki Homepage](https://www.meraki.com) 
 *
 * The version of the OpenAPI document: 1.32.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAICreateOrganizationActionBatch_201_response_status.h
 *
 * Status of action batch
 */

#ifndef OAICreateOrganizationActionBatch_201_response_status_H
#define OAICreateOrganizationActionBatch_201_response_status_H

#include <QJsonObject>

#include "OAICreateOrganizationActionBatch_201_response_status_createdResources_inner.h"
#include <QList>
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAICreateOrganizationActionBatch_201_response_status_createdResources_inner;

class OAICreateOrganizationActionBatch_201_response_status : public OAIObject {
public:
    OAICreateOrganizationActionBatch_201_response_status();
    OAICreateOrganizationActionBatch_201_response_status(QString json);
    ~OAICreateOrganizationActionBatch_201_response_status() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    bool isCompleted() const;
    void setCompleted(const bool &completed);
    bool is_completed_Set() const;
    bool is_completed_Valid() const;

    QList<OAICreateOrganizationActionBatch_201_response_status_createdResources_inner> getCreatedResources() const;
    void setCreatedResources(const QList<OAICreateOrganizationActionBatch_201_response_status_createdResources_inner> &created_resources);
    bool is_created_resources_Set() const;
    bool is_created_resources_Valid() const;

    QList<QString> getErrors() const;
    void setErrors(const QList<QString> &errors);
    bool is_errors_Set() const;
    bool is_errors_Valid() const;

    bool isFailed() const;
    void setFailed(const bool &failed);
    bool is_failed_Set() const;
    bool is_failed_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    bool m_completed;
    bool m_completed_isSet;
    bool m_completed_isValid;

    QList<OAICreateOrganizationActionBatch_201_response_status_createdResources_inner> m_created_resources;
    bool m_created_resources_isSet;
    bool m_created_resources_isValid;

    QList<QString> m_errors;
    bool m_errors_isSet;
    bool m_errors_isValid;

    bool m_failed;
    bool m_failed_isSet;
    bool m_failed_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAICreateOrganizationActionBatch_201_response_status)

#endif // OAICreateOrganizationActionBatch_201_response_status_H
