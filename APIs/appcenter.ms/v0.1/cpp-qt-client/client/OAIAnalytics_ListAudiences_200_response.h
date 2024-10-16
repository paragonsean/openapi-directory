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
 * OAIAnalytics_ListAudiences_200_response.h
 *
 * List of audiences.
 */

#ifndef OAIAnalytics_ListAudiences_200_response_H
#define OAIAnalytics_ListAudiences_200_response_H

#include <QJsonObject>

#include "OAIAnalytics_ListAudiences_200_response_values_inner.h"
#include <QList>
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIAnalytics_ListAudiences_200_response_values_inner;

class OAIAnalytics_ListAudiences_200_response : public OAIObject {
public:
    OAIAnalytics_ListAudiences_200_response();
    OAIAnalytics_ListAudiences_200_response(QString json);
    ~OAIAnalytics_ListAudiences_200_response() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getNextLink() const;
    void setNextLink(const QString &next_link);
    bool is_next_link_Set() const;
    bool is_next_link_Valid() const;

    QList<OAIAnalytics_ListAudiences_200_response_values_inner> getValues() const;
    void setValues(const QList<OAIAnalytics_ListAudiences_200_response_values_inner> &values);
    bool is_values_Set() const;
    bool is_values_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_next_link;
    bool m_next_link_isSet;
    bool m_next_link_isValid;

    QList<OAIAnalytics_ListAudiences_200_response_values_inner> m_values;
    bool m_values_isSet;
    bool m_values_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIAnalytics_ListAudiences_200_response)

#endif // OAIAnalytics_ListAudiences_200_response_H
