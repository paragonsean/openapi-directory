/**
 * ExaVault
 * ExaVaults API allows you to incorporate ExaVaults suite of file transfer and user management tools into your own application.\\nExaVault supports both POST (recommended when requesting large data sets) and GET operations, and requires an API key in order to use.
 *
 * The version of the OpenAPI document: 2.0
 * Contact: support@exavault.com
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIEmailListCollectionResponse.h
 *
 * Response object for list of email lists
 */

#ifndef OAIEmailListCollectionResponse_H
#define OAIEmailListCollectionResponse_H

#include <QJsonObject>

#include "OAIEmailList.h"
#include "OAIUser.h"
#include <QList>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIEmailList;
class OAIUser;

class OAIEmailListCollectionResponse : public OAIObject {
public:
    OAIEmailListCollectionResponse();
    OAIEmailListCollectionResponse(QString json);
    ~OAIEmailListCollectionResponse() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QList<OAIEmailList> getData() const;
    void setData(const QList<OAIEmailList> &data);
    bool is_data_Set() const;
    bool is_data_Valid() const;

    QList<OAIUser> getIncluded() const;
    void setIncluded(const QList<OAIUser> &included);
    bool is_included_Set() const;
    bool is_included_Valid() const;

    qint32 getResponseStatus() const;
    void setResponseStatus(const qint32 &response_status);
    bool is_response_status_Set() const;
    bool is_response_status_Valid() const;

    qint32 getReturnedResults() const;
    void setReturnedResults(const qint32 &returned_results);
    bool is_returned_results_Set() const;
    bool is_returned_results_Valid() const;

    qint32 getTotalResults() const;
    void setTotalResults(const qint32 &total_results);
    bool is_total_results_Set() const;
    bool is_total_results_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QList<OAIEmailList> m_data;
    bool m_data_isSet;
    bool m_data_isValid;

    QList<OAIUser> m_included;
    bool m_included_isSet;
    bool m_included_isValid;

    qint32 m_response_status;
    bool m_response_status_isSet;
    bool m_response_status_isValid;

    qint32 m_returned_results;
    bool m_returned_results_isSet;
    bool m_returned_results_isValid;

    qint32 m_total_results;
    bool m_total_results_isSet;
    bool m_total_results_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIEmailListCollectionResponse)

#endif // OAIEmailListCollectionResponse_H
