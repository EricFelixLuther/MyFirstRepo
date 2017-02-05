import random

column_1 = "artless,bawdy,beslubbering,bootless,churlish,cockered,clouted,craven,currinsh,dankish,dissembling,droning,errant,fawning,fobbing,froward,frothy,gleeking,goatish,gorbellied,impertinent,infectious,jarring,loggerheaded,lumpish,mammering,mangled,mewling,paunchy,pribbling,puking,puny,qualling,rank,reeky,roguish,ruttish,saucy,spleeny,spongy,surly,tottering,umnuzzled,vain,venomed,villainous,warped,wayward,weedy,yeasty"

column_2 = "base-court,bat-fowling,beef-witted,beetle-headed,boil-brained,clapper-clawed,clay-brained,common-kissing,crook-pated,dismal-dreaming,dizzy-eyed,dog-hearted,dread-bolted,earth-vexing,elf-skinned,fat-kidneyed,fen-sucked,flap-mouthed,fly-bitten,folly-fallen,fool-born,full-gorged,guts-griping,half-faced,hasty-witted,hedge-born,hell-hated,idle-headedill-breeding,ill-nurtured,knotty-pated,milk-livered,motley-minded,onion-eyed,plume-pucked,pottle-deep,pox-marked,reeling-ripe,rought-hewn,rude-growning,rump-fed,shard-borne,sheep-biting,spur-galled,swag-bellied,tardy-gaited,tickle-brained,toad-spotted,unchin-snouted,weather-bitten"

column_3 = "apple-jogn,bagage,barnacle,bladder,boar-pigbugbear,bum-bailey,canker-blossom,clack-dish,clotpole,coxcomb,codpiece,death-token,dewberry,flap-dragon,flax-wench,flirt-gill,foot-licker,fustilarian,giglet,gudgeon,haggard,harpy,hedge-pig,horn-beast,hugger-mugger,joithead,lewdster,lout,maggot-pie,malt-worm,mammet,measle,minnow,mescreant,moldwarp,mumble-news,nut-hook,nut-hook,pigeon-egg,pignut,puttock,pumpion,rustbane,scut,skainsmate,strumpet,varlot,vassal,whey-face,wagtail"

def shakespeare_insult_generator():
	print "You", random.choice(column_1.split(",")), random.choice(column_2.split(",")), random.choice(column_3.split(","))

shakespeare_insult_generator()
