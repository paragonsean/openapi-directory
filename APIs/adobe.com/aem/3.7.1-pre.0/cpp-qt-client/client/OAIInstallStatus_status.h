/**
 * Adobe Experience Manager (AEM) API
 * Swagger AEM is an OpenAPI specification for Adobe Experience Manager (AEM) API
 *
 * The version of the OpenAPI document: 3.7.1-pre.0
 * Contact: opensource@shinesolutions.com
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIInstallStatus_status.h
 *
 * 
 */

#ifndef OAIInstallStatus_status_H
#define OAIInstallStatus_status_H

#include <QJsonObject>


#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIInstallStatus_status : public OAIObject {
public:
    OAIInstallStatus_status();
    OAIInstallStatus_status(QString json);
    ~OAIInstallStatus_status() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    bool isFinished() const;
    void setFinished(const bool &finished);
    bool is_finished_Set() const;
    bool is_finished_Valid() const;

    qint32 getItemCount() const;
    void setItemCount(const qint32 &item_count);
    bool is_item_count_Set() const;
    bool is_item_count_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    bool m_finished;
    bool m_finished_isSet;
    bool m_finished_isValid;

    qint32 m_item_count;
    bool m_item_count_isSet;
    bool m_item_count_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIInstallStatus_status)

#endif // OAIInstallStatus_status_H
