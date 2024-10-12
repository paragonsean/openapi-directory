

# GetCharactersCharacterIdNotifications200Ok

200 ok object

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**isRead** | **Boolean** | is_read boolean |  [optional] |
|**notificationId** | **Long** | notification_id integer |  |
|**senderId** | **Integer** | sender_id integer |  |
|**senderType** | [**SenderTypeEnum**](#SenderTypeEnum) | sender_type string |  |
|**text** | **String** | text string |  [optional] |
|**timestamp** | **OffsetDateTime** | timestamp string |  |
|**type** | [**TypeEnum**](#TypeEnum) | type string |  |



## Enum: SenderTypeEnum

| Name | Value |
|---- | -----|
| CHARACTER | &quot;character&quot; |
| CORPORATION | &quot;corporation&quot; |
| ALLIANCE | &quot;alliance&quot; |
| FACTION | &quot;faction&quot; |
| OTHER | &quot;other&quot; |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| ACCEPTED_ALLY | &quot;AcceptedAlly&quot; |
| ACCEPTED_SURRENDER | &quot;AcceptedSurrender&quot; |
| ALL_ANCHORING_MSG | &quot;AllAnchoringMsg&quot; |
| ALL_MAINTENANCE_BILL_MSG | &quot;AllMaintenanceBillMsg&quot; |
| ALL_STRUC_INVULNERABLE_MSG | &quot;AllStrucInvulnerableMsg&quot; |
| ALL_STRUCT_VULNERABLE_MSG | &quot;AllStructVulnerableMsg&quot; |
| ALL_WAR_CORP_JOINED_ALLIANCE_MSG | &quot;AllWarCorpJoinedAllianceMsg&quot; |
| ALL_WAR_DECLARED_MSG | &quot;AllWarDeclaredMsg&quot; |
| ALL_WAR_INVALIDATED_MSG | &quot;AllWarInvalidatedMsg&quot; |
| ALL_WAR_RETRACTED_MSG | &quot;AllWarRetractedMsg&quot; |
| ALL_WAR_SURRENDER_MSG | &quot;AllWarSurrenderMsg&quot; |
| ALLIANCE_CAPITAL_CHANGED | &quot;AllianceCapitalChanged&quot; |
| ALLY_CONTRACT_CANCELLED | &quot;AllyContractCancelled&quot; |
| ALLY_JOINED_WAR_AGGRESSOR_MSG | &quot;AllyJoinedWarAggressorMsg&quot; |
| ALLY_JOINED_WAR_ALLY_MSG | &quot;AllyJoinedWarAllyMsg&quot; |
| ALLY_JOINED_WAR_DEFENDER_MSG | &quot;AllyJoinedWarDefenderMsg&quot; |
| BATTLE_PUNISH_FRIENDLY_FIRE | &quot;BattlePunishFriendlyFire&quot; |
| BILL_OUT_OF_MONEY_MSG | &quot;BillOutOfMoneyMsg&quot; |
| BILL_PAID_CORP_ALL_MSG | &quot;BillPaidCorpAllMsg&quot; |
| BOUNTY_CLAIM_MSG | &quot;BountyClaimMsg&quot; |
| BOUNTY_ESS_SHARED | &quot;BountyESSShared&quot; |
| BOUNTY_ESS_TAKEN | &quot;BountyESSTaken&quot; |
| BOUNTY_PLACED_ALLIANCE | &quot;BountyPlacedAlliance&quot; |
| BOUNTY_PLACED_CHAR | &quot;BountyPlacedChar&quot; |
| BOUNTY_PLACED_CORP | &quot;BountyPlacedCorp&quot; |
| BOUNTY_YOUR_BOUNTY_CLAIMED | &quot;BountyYourBountyClaimed&quot; |
| BUDDY_CONNECT_CONTACT_ADD | &quot;BuddyConnectContactAdd&quot; |
| CHAR_APP_ACCEPT_MSG | &quot;CharAppAcceptMsg&quot; |
| CHAR_APP_REJECT_MSG | &quot;CharAppRejectMsg&quot; |
| CHAR_APP_WITHDRAW_MSG | &quot;CharAppWithdrawMsg&quot; |
| CHAR_LEFT_CORP_MSG | &quot;CharLeftCorpMsg&quot; |
| CHAR_MEDAL_MSG | &quot;CharMedalMsg&quot; |
| CHAR_TERMINATION_MSG | &quot;CharTerminationMsg&quot; |
| CLONE_ACTIVATION_MSG | &quot;CloneActivationMsg&quot; |
| CLONE_ACTIVATION_MSG2 | &quot;CloneActivationMsg2&quot; |
| CLONE_MOVED_MSG | &quot;CloneMovedMsg&quot; |
| CLONE_REVOKED_MSG1 | &quot;CloneRevokedMsg1&quot; |
| CLONE_REVOKED_MSG2 | &quot;CloneRevokedMsg2&quot; |
| COMBAT_OPERATION_FINISHED | &quot;CombatOperationFinished&quot; |
| CONTACT_ADD | &quot;ContactAdd&quot; |
| CONTACT_EDIT | &quot;ContactEdit&quot; |
| CONTAINER_PASSWORD_MSG | &quot;ContainerPasswordMsg&quot; |
| CORP_ALL_BILL_MSG | &quot;CorpAllBillMsg&quot; |
| CORP_APP_ACCEPT_MSG | &quot;CorpAppAcceptMsg&quot; |
| CORP_APP_INVITED_MSG | &quot;CorpAppInvitedMsg&quot; |
| CORP_APP_NEW_MSG | &quot;CorpAppNewMsg&quot; |
| CORP_APP_REJECT_CUSTOM_MSG | &quot;CorpAppRejectCustomMsg&quot; |
| CORP_APP_REJECT_MSG | &quot;CorpAppRejectMsg&quot; |
| CORP_DIVIDEND_MSG | &quot;CorpDividendMsg&quot; |
| CORP_FRIENDLY_FIRE_DISABLE_TIMER_COMPLETED | &quot;CorpFriendlyFireDisableTimerCompleted&quot; |
| CORP_FRIENDLY_FIRE_DISABLE_TIMER_STARTED | &quot;CorpFriendlyFireDisableTimerStarted&quot; |
| CORP_FRIENDLY_FIRE_ENABLE_TIMER_COMPLETED | &quot;CorpFriendlyFireEnableTimerCompleted&quot; |
| CORP_FRIENDLY_FIRE_ENABLE_TIMER_STARTED | &quot;CorpFriendlyFireEnableTimerStarted&quot; |
| CORP_KICKED | &quot;CorpKicked&quot; |
| CORP_LIQUIDATION_MSG | &quot;CorpLiquidationMsg&quot; |
| CORP_NEW_CEO_MSG | &quot;CorpNewCEOMsg&quot; |
| CORP_NEWS_MSG | &quot;CorpNewsMsg&quot; |
| CORP_OFFICE_EXPIRATION_MSG | &quot;CorpOfficeExpirationMsg&quot; |
| CORP_STRUCT_LOST_MSG | &quot;CorpStructLostMsg&quot; |
| CORP_TAX_CHANGE_MSG | &quot;CorpTaxChangeMsg&quot; |
| CORP_VOTE_CEO_REVOKED_MSG | &quot;CorpVoteCEORevokedMsg&quot; |
| CORP_VOTE_MSG | &quot;CorpVoteMsg&quot; |
| CORP_WAR_DECLARED_MSG | &quot;CorpWarDeclaredMsg&quot; |
| CORP_WAR_FIGHTING_LEGAL_MSG | &quot;CorpWarFightingLegalMsg&quot; |
| CORP_WAR_INVALIDATED_MSG | &quot;CorpWarInvalidatedMsg&quot; |
| CORP_WAR_RETRACTED_MSG | &quot;CorpWarRetractedMsg&quot; |
| CORP_WAR_SURRENDER_MSG | &quot;CorpWarSurrenderMsg&quot; |
| CUSTOMS_MSG | &quot;CustomsMsg&quot; |
| DECLARE_WAR | &quot;DeclareWar&quot; |
| DISTRICT_ATTACKED | &quot;DistrictAttacked&quot; |
| DUST_APP_ACCEPTED_MSG | &quot;DustAppAcceptedMsg&quot; |
| ENTOSIS_CAPTURE_STARTED | &quot;EntosisCaptureStarted&quot; |
| FW_ALLIANCE_KICK_MSG | &quot;FWAllianceKickMsg&quot; |
| FW_ALLIANCE_WARNING_MSG | &quot;FWAllianceWarningMsg&quot; |
| FW_CHAR_KICK_MSG | &quot;FWCharKickMsg&quot; |
| FW_CHAR_RANK_GAIN_MSG | &quot;FWCharRankGainMsg&quot; |
| FW_CHAR_RANK_LOSS_MSG | &quot;FWCharRankLossMsg&quot; |
| FW_CHAR_WARNING_MSG | &quot;FWCharWarningMsg&quot; |
| FW_CORP_JOIN_MSG | &quot;FWCorpJoinMsg&quot; |
| FW_CORP_KICK_MSG | &quot;FWCorpKickMsg&quot; |
| FW_CORP_LEAVE_MSG | &quot;FWCorpLeaveMsg&quot; |
| FW_CORP_WARNING_MSG | &quot;FWCorpWarningMsg&quot; |
| FAC_WAR_CORP_JOIN_REQUEST_MSG | &quot;FacWarCorpJoinRequestMsg&quot; |
| FAC_WAR_CORP_JOIN_WITHDRAW_MSG | &quot;FacWarCorpJoinWithdrawMsg&quot; |
| FAC_WAR_CORP_LEAVE_REQUEST_MSG | &quot;FacWarCorpLeaveRequestMsg&quot; |
| FAC_WAR_CORP_LEAVE_WITHDRAW_MSG | &quot;FacWarCorpLeaveWithdrawMsg&quot; |
| FAC_WAR_LP_DISQUALIFIED_EVENT | &quot;FacWarLPDisqualifiedEvent&quot; |
| FAC_WAR_LP_DISQUALIFIED_KILL | &quot;FacWarLPDisqualifiedKill&quot; |
| FAC_WAR_LP_PAYOUT_EVENT | &quot;FacWarLPPayoutEvent&quot; |
| FAC_WAR_LP_PAYOUT_KILL | &quot;FacWarLPPayoutKill&quot; |
| GAME_TIME_ADDED | &quot;GameTimeAdded&quot; |
| GAME_TIME_RECEIVED | &quot;GameTimeReceived&quot; |
| GAME_TIME_SENT | &quot;GameTimeSent&quot; |
| GIFT_RECEIVED | &quot;GiftReceived&quot; |
| I_HUB_DESTROYED_BY_BILL_FAILURE | &quot;IHubDestroyedByBillFailure&quot; |
| INCURSION_COMPLETED_MSG | &quot;IncursionCompletedMsg&quot; |
| INDUSTRY_OPERATION_FINISHED | &quot;IndustryOperationFinished&quot; |
| INDUSTRY_TEAM_AUCTION_LOST | &quot;IndustryTeamAuctionLost&quot; |
| INDUSTRY_TEAM_AUCTION_WON | &quot;IndustryTeamAuctionWon&quot; |
| INFRASTRUCTURE_HUB_BILL_ABOUT_TO_EXPIRE | &quot;InfrastructureHubBillAboutToExpire&quot; |
| INSURANCE_EXPIRATION_MSG | &quot;InsuranceExpirationMsg&quot; |
| INSURANCE_FIRST_SHIP_MSG | &quot;InsuranceFirstShipMsg&quot; |
| INSURANCE_INVALIDATED_MSG | &quot;InsuranceInvalidatedMsg&quot; |
| INSURANCE_ISSUED_MSG | &quot;InsuranceIssuedMsg&quot; |
| INSURANCE_PAYOUT_MSG | &quot;InsurancePayoutMsg&quot; |
| JUMP_CLONE_DELETED_MSG1 | &quot;JumpCloneDeletedMsg1&quot; |
| JUMP_CLONE_DELETED_MSG2 | &quot;JumpCloneDeletedMsg2&quot; |
| KILL_REPORT_FINAL_BLOW | &quot;KillReportFinalBlow&quot; |
| KILL_REPORT_VICTIM | &quot;KillReportVictim&quot; |
| KILL_RIGHT_AVAILABLE | &quot;KillRightAvailable&quot; |
| KILL_RIGHT_AVAILABLE_OPEN | &quot;KillRightAvailableOpen&quot; |
| KILL_RIGHT_EARNED | &quot;KillRightEarned&quot; |
| KILL_RIGHT_UNAVAILABLE | &quot;KillRightUnavailable&quot; |
| KILL_RIGHT_UNAVAILABLE_OPEN | &quot;KillRightUnavailableOpen&quot; |
| KILL_RIGHT_USED | &quot;KillRightUsed&quot; |
| LOCATE_CHAR_MSG | &quot;LocateCharMsg&quot; |
| MADE_WAR_MUTUAL | &quot;MadeWarMutual&quot; |
| MERC_OFFERED_NEGOTIATION_MSG | &quot;MercOfferedNegotiationMsg&quot; |
| MISSION_OFFER_EXPIRATION_MSG | &quot;MissionOfferExpirationMsg&quot; |
| MISSION_TIMEOUT_MSG | &quot;MissionTimeoutMsg&quot; |
| MOONMINING_AUTOMATIC_FRACTURE | &quot;MoonminingAutomaticFracture&quot; |
| MOONMINING_EXTRACTION_CANCELLED | &quot;MoonminingExtractionCancelled&quot; |
| MOONMINING_EXTRACTION_FINISHED | &quot;MoonminingExtractionFinished&quot; |
| MOONMINING_EXTRACTION_STARTED | &quot;MoonminingExtractionStarted&quot; |
| MOONMINING_LASER_FIRED | &quot;MoonminingLaserFired&quot; |
| NPC_STANDINGS_GAINED | &quot;NPCStandingsGained&quot; |
| NPC_STANDINGS_LOST | &quot;NPCStandingsLost&quot; |
| OFFERED_SURRENDER | &quot;OfferedSurrender&quot; |
| OFFERED_TO_ALLY | &quot;OfferedToAlly&quot; |
| OLD_LSC_MESSAGES | &quot;OldLscMessages&quot; |
| OPERATION_FINISHED | &quot;OperationFinished&quot; |
| ORBITAL_ATTACKED | &quot;OrbitalAttacked&quot; |
| ORBITAL_REINFORCED | &quot;OrbitalReinforced&quot; |
| OWNERSHIP_TRANSFERRED | &quot;OwnershipTransferred&quot; |
| REIMBURSEMENT_MSG | &quot;ReimbursementMsg&quot; |
| RESEARCH_MISSION_AVAILABLE_MSG | &quot;ResearchMissionAvailableMsg&quot; |
| RETRACTS_WAR | &quot;RetractsWar&quot; |
| SEASONAL_CHALLENGE_COMPLETED | &quot;SeasonalChallengeCompleted&quot; |
| SOV_ALL_CLAIM_AQUIRED_MSG | &quot;SovAllClaimAquiredMsg&quot; |
| SOV_ALL_CLAIM_LOST_MSG | &quot;SovAllClaimLostMsg&quot; |
| SOV_COMMAND_NODE_EVENT_STARTED | &quot;SovCommandNodeEventStarted&quot; |
| SOV_CORP_BILL_LATE_MSG | &quot;SovCorpBillLateMsg&quot; |
| SOV_CORP_CLAIM_FAIL_MSG | &quot;SovCorpClaimFailMsg&quot; |
| SOV_DISRUPTOR_MSG | &quot;SovDisruptorMsg&quot; |
| SOV_STATION_ENTERED_FREEPORT | &quot;SovStationEnteredFreeport&quot; |
| SOV_STRUCTURE_DESTROYED | &quot;SovStructureDestroyed&quot; |
| SOV_STRUCTURE_REINFORCED | &quot;SovStructureReinforced&quot; |
| SOV_STRUCTURE_SELF_DESTRUCT_CANCEL | &quot;SovStructureSelfDestructCancel&quot; |
| SOV_STRUCTURE_SELF_DESTRUCT_FINISHED | &quot;SovStructureSelfDestructFinished&quot; |
| SOV_STRUCTURE_SELF_DESTRUCT_REQUESTED | &quot;SovStructureSelfDestructRequested&quot; |
| SOVEREIGNTY_IH_DAMAGE_MSG | &quot;SovereigntyIHDamageMsg&quot; |
| SOVEREIGNTY_SBU_DAMAGE_MSG | &quot;SovereigntySBUDamageMsg&quot; |
| SOVEREIGNTY_TCU_DAMAGE_MSG | &quot;SovereigntyTCUDamageMsg&quot; |
| STATION_AGGRESSION_MSG1 | &quot;StationAggressionMsg1&quot; |
| STATION_AGGRESSION_MSG2 | &quot;StationAggressionMsg2&quot; |
| STATION_CONQUER_MSG | &quot;StationConquerMsg&quot; |
| STATION_SERVICE_DISABLED | &quot;StationServiceDisabled&quot; |
| STATION_SERVICE_ENABLED | &quot;StationServiceEnabled&quot; |
| STATION_STATE_CHANGE_MSG | &quot;StationStateChangeMsg&quot; |
| STORY_LINE_MISSION_AVAILABLE_MSG | &quot;StoryLineMissionAvailableMsg&quot; |
| STRUCTURE_ANCHORING | &quot;StructureAnchoring&quot; |
| STRUCTURE_COURIER_CONTRACT_CHANGED | &quot;StructureCourierContractChanged&quot; |
| STRUCTURE_DESTROYED | &quot;StructureDestroyed&quot; |
| STRUCTURE_FUEL_ALERT | &quot;StructureFuelAlert&quot; |
| STRUCTURE_ITEMS_DELIVERED | &quot;StructureItemsDelivered&quot; |
| STRUCTURE_ITEMS_MOVED_TO_SAFETY | &quot;StructureItemsMovedToSafety&quot; |
| STRUCTURE_LOST_ARMOR | &quot;StructureLostArmor&quot; |
| STRUCTURE_LOST_SHIELDS | &quot;StructureLostShields&quot; |
| STRUCTURE_ONLINE | &quot;StructureOnline&quot; |
| STRUCTURE_SERVICES_OFFLINE | &quot;StructureServicesOffline&quot; |
| STRUCTURE_UNANCHORING | &quot;StructureUnanchoring&quot; |
| STRUCTURE_UNDER_ATTACK | &quot;StructureUnderAttack&quot; |
| STRUCTURE_WENT_HIGH_POWER | &quot;StructureWentHighPower&quot; |
| STRUCTURE_WENT_LOW_POWER | &quot;StructureWentLowPower&quot; |
| STRUCTURES_JOBS_CANCELLED | &quot;StructuresJobsCancelled&quot; |
| STRUCTURES_JOBS_PAUSED | &quot;StructuresJobsPaused&quot; |
| STRUCTURES_REINFORCEMENT_CHANGED | &quot;StructuresReinforcementChanged&quot; |
| TOWER_ALERT_MSG | &quot;TowerAlertMsg&quot; |
| TOWER_RESOURCE_ALERT_MSG | &quot;TowerResourceAlertMsg&quot; |
| TRANSACTION_REVERSAL_MSG | &quot;TransactionReversalMsg&quot; |
| TUTORIAL_MSG | &quot;TutorialMsg&quot; |
| WAR_ALLY_OFFER_DECLINED_MSG | &quot;WarAllyOfferDeclinedMsg&quot; |
| WAR_SURRENDER_DECLINED_MSG | &quot;WarSurrenderDeclinedMsg&quot; |
| WAR_SURRENDER_OFFER_MSG | &quot;WarSurrenderOfferMsg&quot; |



