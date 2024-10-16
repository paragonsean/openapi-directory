/**
 * Advicent.FactFinderService
 * An API for accessing the NaviPlan Fact Finder.
 *
 * The version of the OpenAPI document: v1
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIAccountModel.h
 *
 * 
 */

#ifndef OAIAccountModel_H
#define OAIAccountModel_H

#include <QJsonObject>

#include <QDateTime>
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIAccountModel : public OAIObject {
public:
    OAIAccountModel();
    OAIAccountModel(QString json);
    ~OAIAccountModel() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    qint32 getAccountType() const;
    void setAccountType(const qint32 &account_type);
    bool is_account_type_Set() const;
    bool is_account_type_Valid() const;

    QString getDescription() const;
    void setDescription(const QString &description);
    bool is_description_Set() const;
    bool is_description_Valid() const;

    QString getExternalDestinationId() const;
    void setExternalDestinationId(const QString &external_destination_id);
    bool is_external_destination_id_Set() const;
    bool is_external_destination_id_Valid() const;

    QString getExternalSourceId() const;
    void setExternalSourceId(const QString &external_source_id);
    bool is_external_source_id_Set() const;
    bool is_external_source_id_Valid() const;

    QString getExternalSourceName() const;
    void setExternalSourceName(const QString &external_source_name);
    bool is_external_source_name_Set() const;
    bool is_external_source_name_Valid() const;

    qint32 getFactFinderId() const;
    void setFactFinderId(const qint32 &fact_finder_id);
    bool is_fact_finder_id_Set() const;
    bool is_fact_finder_id_Valid() const;

    QDateTime getLastUpdated() const;
    void setLastUpdated(const QDateTime &last_updated);
    bool is_last_updated_Set() const;
    bool is_last_updated_Valid() const;

    double getMarketValue() const;
    void setMarketValue(const double &market_value);
    bool is_market_value_Set() const;
    bool is_market_value_Valid() const;

    QString getOwner() const;
    void setOwner(const QString &owner);
    bool is_owner_Set() const;
    bool is_owner_Valid() const;

    qint32 getOwnerDependentId() const;
    void setOwnerDependentId(const qint32 &owner_dependent_id);
    bool is_owner_dependent_id_Set() const;
    bool is_owner_dependent_id_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    qint32 m_account_type;
    bool m_account_type_isSet;
    bool m_account_type_isValid;

    QString m_description;
    bool m_description_isSet;
    bool m_description_isValid;

    QString m_external_destination_id;
    bool m_external_destination_id_isSet;
    bool m_external_destination_id_isValid;

    QString m_external_source_id;
    bool m_external_source_id_isSet;
    bool m_external_source_id_isValid;

    QString m_external_source_name;
    bool m_external_source_name_isSet;
    bool m_external_source_name_isValid;

    qint32 m_fact_finder_id;
    bool m_fact_finder_id_isSet;
    bool m_fact_finder_id_isValid;

    QDateTime m_last_updated;
    bool m_last_updated_isSet;
    bool m_last_updated_isValid;

    double m_market_value;
    bool m_market_value_isSet;
    bool m_market_value_isValid;

    QString m_owner;
    bool m_owner_isSet;
    bool m_owner_isValid;

    qint32 m_owner_dependent_id;
    bool m_owner_dependent_id_isSet;
    bool m_owner_dependent_id_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIAccountModel)

#endif // OAIAccountModel_H
