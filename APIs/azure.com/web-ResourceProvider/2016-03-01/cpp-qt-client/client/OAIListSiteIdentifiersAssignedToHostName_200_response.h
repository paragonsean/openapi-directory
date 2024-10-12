/**
 *  API Client
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 2016-03-01
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIListSiteIdentifiersAssignedToHostName_200_response.h
 *
 * Collection of identifiers.
 */

#ifndef OAIListSiteIdentifiersAssignedToHostName_200_response_H
#define OAIListSiteIdentifiersAssignedToHostName_200_response_H

#include <QJsonObject>

#include "OAIListSiteIdentifiersAssignedToHostName_200_response_value_inner.h"
#include <QList>
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIListSiteIdentifiersAssignedToHostName_200_response_value_inner;

class OAIListSiteIdentifiersAssignedToHostName_200_response : public OAIObject {
public:
    OAIListSiteIdentifiersAssignedToHostName_200_response();
    OAIListSiteIdentifiersAssignedToHostName_200_response(QString json);
    ~OAIListSiteIdentifiersAssignedToHostName_200_response() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getNextLink() const;
    void setNextLink(const QString &next_link);
    bool is_next_link_Set() const;
    bool is_next_link_Valid() const;

    QList<OAIListSiteIdentifiersAssignedToHostName_200_response_value_inner> getValue() const;
    void setValue(const QList<OAIListSiteIdentifiersAssignedToHostName_200_response_value_inner> &value);
    bool is_value_Set() const;
    bool is_value_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_next_link;
    bool m_next_link_isSet;
    bool m_next_link_isValid;

    QList<OAIListSiteIdentifiersAssignedToHostName_200_response_value_inner> m_value;
    bool m_value_isSet;
    bool m_value_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIListSiteIdentifiersAssignedToHostName_200_response)

#endif // OAIListSiteIdentifiersAssignedToHostName_200_response_H
