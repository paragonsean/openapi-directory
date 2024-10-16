/**
 * The Blue Alliance API v3
 * # Overview    Information and statistics about FIRST Robotics Competition teams and events.   # Authentication   All endpoints require an Auth Key to be passed in the header `X-TBA-Auth-Key`. If you do not have an auth key yet, you can obtain one from your [Account Page](/account).
 *
 * The version of the OpenAPI document: 3.8.2
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAITeam_Event_Status_rank_sort_order_info_inner.h
 *
 * 
 */

#ifndef OAITeam_Event_Status_rank_sort_order_info_inner_H
#define OAITeam_Event_Status_rank_sort_order_info_inner_H

#include <QJsonObject>

#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAITeam_Event_Status_rank_sort_order_info_inner : public OAIObject {
public:
    OAITeam_Event_Status_rank_sort_order_info_inner();
    OAITeam_Event_Status_rank_sort_order_info_inner(QString json);
    ~OAITeam_Event_Status_rank_sort_order_info_inner() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getName() const;
    void setName(const QString &name);
    bool is_name_Set() const;
    bool is_name_Valid() const;

    qint32 getPrecision() const;
    void setPrecision(const qint32 &precision);
    bool is_precision_Set() const;
    bool is_precision_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_name;
    bool m_name_isSet;
    bool m_name_isValid;

    qint32 m_precision;
    bool m_precision_isSet;
    bool m_precision_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAITeam_Event_Status_rank_sort_order_info_inner)

#endif // OAITeam_Event_Status_rank_sort_order_info_inner_H
