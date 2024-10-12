/**
 * www.zoomconnect.com
 * The world's greatest SMS API
 *
 * The version of the OpenAPI document: 1
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIWebServiceAccountStatistics.h
 *
 * WebServiceAccountStatistics
 */

#ifndef OAIWebServiceAccountStatistics_H
#define OAIWebServiceAccountStatistics_H

#include <QJsonObject>

#include "OAIWebServiceStatistics.h"
#include "OAIWebServiceUserStatistics.h"
#include <QDateTime>
#include <QList>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIWebServiceStatistics;
class OAIWebServiceUserStatistics;

class OAIWebServiceAccountStatistics : public OAIObject {
public:
    OAIWebServiceAccountStatistics();
    OAIWebServiceAccountStatistics(QString json);
    ~OAIWebServiceAccountStatistics() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QDateTime getFrom() const;
    void setFrom(const QDateTime &from);
    bool is_from_Set() const;
    bool is_from_Valid() const;

    OAIWebServiceStatistics getGrandTotal() const;
    void setGrandTotal(const OAIWebServiceStatistics &grand_total);
    bool is_grand_total_Set() const;
    bool is_grand_total_Valid() const;

    bool isShowingCreditValue() const;
    void setShowingCreditValue(const bool &showing_credit_value);
    bool is_showing_credit_value_Set() const;
    bool is_showing_credit_value_Valid() const;

    QDateTime getTo() const;
    void setTo(const QDateTime &to);
    bool is_to_Set() const;
    bool is_to_Valid() const;

    QList<OAIWebServiceUserStatistics> getUsers() const;
    void setUsers(const QList<OAIWebServiceUserStatistics> &users);
    bool is_users_Set() const;
    bool is_users_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QDateTime m_from;
    bool m_from_isSet;
    bool m_from_isValid;

    OAIWebServiceStatistics m_grand_total;
    bool m_grand_total_isSet;
    bool m_grand_total_isValid;

    bool m_showing_credit_value;
    bool m_showing_credit_value_isSet;
    bool m_showing_credit_value_isValid;

    QDateTime m_to;
    bool m_to_isSet;
    bool m_to_isValid;

    QList<OAIWebServiceUserStatistics> m_users;
    bool m_users_isSet;
    bool m_users_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIWebServiceAccountStatistics)

#endif // OAIWebServiceAccountStatistics_H
