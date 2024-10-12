/**
 * eNanoMapper database
 * AMBIT REST web services [eNanoMapper profile] with free text & faceted search
 *
 * The version of the OpenAPI document: 4.0.0
 * Contact: support@ideaconsult.net
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIDataset.h
 *
 * 
 */

#ifndef OAIDataset_H
#define OAIDataset_H

#include <QJsonObject>

#include "OAIObject.h"
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIDataset : public OAIObject {
public:
    OAIDataset();
    OAIDataset(QString json);
    ~OAIDataset() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    OAIObject getDataEntry() const;
    void setDataEntry(const OAIObject &data_entry);
    bool is_data_entry_Set() const;
    bool is_data_entry_Valid() const;

    OAIObject getFeature() const;
    void setFeature(const OAIObject &feature);
    bool is_feature_Set() const;
    bool is_feature_Valid() const;

    QString getModelUri() const;
    void setModelUri(const QString &model_uri);
    bool is_model_uri_Set() const;
    bool is_model_uri_Valid() const;

    OAIObject getQuery() const;
    void setQuery(const OAIObject &query);
    bool is_query_Set() const;
    bool is_query_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    OAIObject m_data_entry;
    bool m_data_entry_isSet;
    bool m_data_entry_isValid;

    OAIObject m_feature;
    bool m_feature_isSet;
    bool m_feature_isValid;

    QString m_model_uri;
    bool m_model_uri_isSet;
    bool m_model_uri_isValid;

    OAIObject m_query;
    bool m_query_isSet;
    bool m_query_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIDataset)

#endif // OAIDataset_H
