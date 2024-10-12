/**
 * Google Pay Passes API
 * API for issuers to save and manage Google Wallet Objects.
 *
 * The version of the OpenAPI document: v1
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIEventSeat.h
 *
 * 
 */

#ifndef OAIEventSeat_H
#define OAIEventSeat_H

#include <QJsonObject>

#include "OAILocalizedString.h"
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAILocalizedString;

class OAIEventSeat : public OAIObject {
public:
    OAIEventSeat();
    OAIEventSeat(QString json);
    ~OAIEventSeat() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    OAILocalizedString getGate() const;
    void setGate(const OAILocalizedString &gate);
    bool is_gate_Set() const;
    bool is_gate_Valid() const;

    QString getKind() const;
    void setKind(const QString &kind);
    bool is_kind_Set() const;
    bool is_kind_Valid() const;

    OAILocalizedString getRow() const;
    void setRow(const OAILocalizedString &row);
    bool is_row_Set() const;
    bool is_row_Valid() const;

    OAILocalizedString getSeat() const;
    void setSeat(const OAILocalizedString &seat);
    bool is_seat_Set() const;
    bool is_seat_Valid() const;

    OAILocalizedString getSection() const;
    void setSection(const OAILocalizedString &section);
    bool is_section_Set() const;
    bool is_section_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    OAILocalizedString m_gate;
    bool m_gate_isSet;
    bool m_gate_isValid;

    QString m_kind;
    bool m_kind_isSet;
    bool m_kind_isValid;

    OAILocalizedString m_row;
    bool m_row_isSet;
    bool m_row_isValid;

    OAILocalizedString m_seat;
    bool m_seat_isSet;
    bool m_seat_isValid;

    OAILocalizedString m_section;
    bool m_section_isSet;
    bool m_section_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIEventSeat)

#endif // OAIEventSeat_H
