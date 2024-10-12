/**
 * Authorized Partner API Specification
 * To access files in user’s DigiLocker account from your application, you must first obtain user’s authorization.
 *
 * The version of the OpenAPI document: 1.0.0
 * Contact: support@digitallocker.gov.in
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIGetStatisticsResponse_yearwise_authentic_documents_details2.h
 *
 * 
 */

#ifndef OAIGetStatisticsResponse_yearwise_authentic_documents_details2_H
#define OAIGetStatisticsResponse_yearwise_authentic_documents_details2_H

#include <QJsonObject>


#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIGetStatisticsResponse_yearwise_authentic_documents_details2 : public OAIObject {
public:
    OAIGetStatisticsResponse_yearwise_authentic_documents_details2();
    OAIGetStatisticsResponse_yearwise_authentic_documents_details2(QString json);
    ~OAIGetStatisticsResponse_yearwise_authentic_documents_details2() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    qint32 getCount() const;
    void setCount(const qint32 &count);
    bool is_count_Set() const;
    bool is_count_Valid() const;

    qint32 getId() const;
    void setId(const qint32 &id);
    bool is_id_Set() const;
    bool is_id_Valid() const;

    qint32 getYear() const;
    void setYear(const qint32 &year);
    bool is_year_Set() const;
    bool is_year_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    qint32 m_count;
    bool m_count_isSet;
    bool m_count_isValid;

    qint32 m_id;
    bool m_id_isSet;
    bool m_id_isValid;

    qint32 m_year;
    bool m_year_isSet;
    bool m_year_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIGetStatisticsResponse_yearwise_authentic_documents_details2)

#endif // OAIGetStatisticsResponse_yearwise_authentic_documents_details2_H
