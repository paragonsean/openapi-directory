/**
 * ApiManagementClient
 * Use this REST API to get all the issues across an Azure Api Management service.
 *
 * The version of the OpenAPI document: 2018-01-01
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIIssue_ListByService_200_response.h
 *
 * Paged Issue list representation.
 */

#ifndef OAIIssue_ListByService_200_response_H
#define OAIIssue_ListByService_200_response_H

#include <QJsonObject>

#include "OAIIssue_ListByService_200_response_value_inner.h"
#include <QList>
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIIssue_ListByService_200_response_value_inner;

class OAIIssue_ListByService_200_response : public OAIObject {
public:
    OAIIssue_ListByService_200_response();
    OAIIssue_ListByService_200_response(QString json);
    ~OAIIssue_ListByService_200_response() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getNextLink() const;
    void setNextLink(const QString &next_link);
    bool is_next_link_Set() const;
    bool is_next_link_Valid() const;

    QList<OAIIssue_ListByService_200_response_value_inner> getValue() const;
    void setValue(const QList<OAIIssue_ListByService_200_response_value_inner> &value);
    bool is_value_Set() const;
    bool is_value_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_next_link;
    bool m_next_link_isSet;
    bool m_next_link_isValid;

    QList<OAIIssue_ListByService_200_response_value_inner> m_value;
    bool m_value_isSet;
    bool m_value_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIIssue_ListByService_200_response)

#endif // OAIIssue_ListByService_200_response_H
