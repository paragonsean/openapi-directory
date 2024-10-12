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
 * OAISolrquery_post_request_params.h
 *
 * 
 */

#ifndef OAISolrquery_post_request_params_H
#define OAISolrquery_post_request_params_H

#include <QJsonObject>

#include <QList>
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAISolrquery_post_request_params : public OAIObject {
public:
    OAISolrquery_post_request_params();
    OAISolrquery_post_request_params(QString json);
    ~OAISolrquery_post_request_params() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QList<QString> getFl() const;
    void setFl(const QList<QString> &fl);
    bool is_fl_Set() const;
    bool is_fl_Valid() const;

    qint32 getRows() const;
    void setRows(const qint32 &rows);
    bool is_rows_Set() const;
    bool is_rows_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QList<QString> m_fl;
    bool m_fl_isSet;
    bool m_fl_isValid;

    qint32 m_rows;
    bool m_rows_isSet;
    bool m_rows_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAISolrquery_post_request_params)

#endif // OAISolrquery_post_request_params_H
