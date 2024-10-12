/**
 * Azure Machine Learning Model Management Service
 * These APIs allow end users to manage Azure Machine Learning Models, Images, Profiles, and Services.
 *
 * The version of the OpenAPI document: 2019-09-30
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIModelDataCollection.h
 *
 * The Model data collection properties.
 */

#ifndef OAIModelDataCollection_H
#define OAIModelDataCollection_H

#include <QJsonObject>


#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIModelDataCollection : public OAIObject {
public:
    OAIModelDataCollection();
    OAIModelDataCollection(QString json);
    ~OAIModelDataCollection() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    bool isEventHubEnabled() const;
    void setEventHubEnabled(const bool &event_hub_enabled);
    bool is_event_hub_enabled_Set() const;
    bool is_event_hub_enabled_Valid() const;

    bool isStorageEnabled() const;
    void setStorageEnabled(const bool &storage_enabled);
    bool is_storage_enabled_Set() const;
    bool is_storage_enabled_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    bool m_event_hub_enabled;
    bool m_event_hub_enabled_isSet;
    bool m_event_hub_enabled_isValid;

    bool m_storage_enabled;
    bool m_storage_enabled_isSet;
    bool m_storage_enabled_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIModelDataCollection)

#endif // OAIModelDataCollection_H
