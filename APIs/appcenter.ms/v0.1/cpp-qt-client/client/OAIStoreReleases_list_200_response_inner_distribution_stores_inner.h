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
 * OAIStoreReleases_list_200_response_inner_distribution_stores_inner.h
 *
 * 
 */

#ifndef OAIStoreReleases_list_200_response_inner_distribution_stores_inner_H
#define OAIStoreReleases_list_200_response_inner_distribution_stores_inner_H

#include <QJsonObject>

#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIStoreReleases_list_200_response_inner_distribution_stores_inner : public OAIObject {
public:
    OAIStoreReleases_list_200_response_inner_distribution_stores_inner();
    OAIStoreReleases_list_200_response_inner_distribution_stores_inner(QString json);
    ~OAIStoreReleases_list_200_response_inner_distribution_stores_inner() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getId() const;
    void setId(const QString &id);
    bool is_id_Set() const;
    bool is_id_Valid() const;

    bool isIsLatest() const;
    void setIsLatest(const bool &is_latest);
    bool is_is_latest_Set() const;
    bool is_is_latest_Valid() const;

    QString getName() const;
    void setName(const QString &name);
    bool is_name_Set() const;
    bool is_name_Valid() const;

    QString getPublishingStatus() const;
    void setPublishingStatus(const QString &publishing_status);
    bool is_publishing_status_Set() const;
    bool is_publishing_status_Valid() const;

    QString getType() const;
    void setType(const QString &type);
    bool is_type_Set() const;
    bool is_type_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_id;
    bool m_id_isSet;
    bool m_id_isValid;

    bool m_is_latest;
    bool m_is_latest_isSet;
    bool m_is_latest_isValid;

    QString m_name;
    bool m_name_isSet;
    bool m_name_isValid;

    QString m_publishing_status;
    bool m_publishing_status_isSet;
    bool m_publishing_status_isValid;

    QString m_type;
    bool m_type_isSet;
    bool m_type_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIStoreReleases_list_200_response_inner_distribution_stores_inner)

#endif // OAIStoreReleases_list_200_response_inner_distribution_stores_inner_H
