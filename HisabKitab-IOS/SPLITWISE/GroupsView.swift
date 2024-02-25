//
//  GroupsView.swift
//  SPLITWISE
//
//  Created by Irfan on 25/02/24.
//

import SwiftUI

struct GroupsView: View {
    var body: some View {
        ZStack{
            Color.color.ignoresSafeArea()
            
                VStack{
                    
                    ZStack{
                        Rectangle().frame(width:380,height:240).cornerRadius(20).padding(.top,15)
                        
                        VStack{
                            
                            HStack{
                                Image(systemName:"function").foregroundColor(.white).font(.system(size: 40))
                                
                                Text("HisabKitab").fontWeight(.heavy).foregroundColor(.neon).font(.system(size: 40))
                                
                            }.padding(.top,19)
                            
                            Rectangle().size(width: 350, height: 2).foregroundColor(.gray)
                            
                            Text("Dashboard").fontWeight(.bold).foregroundColor(.white).frame(width:340,alignment: .leading).font(.system(size: 30))
                            
                            HStack{
                                ZStack{
                                    Rectangle().frame(width:110,height:65).foregroundColor(.color).cornerRadius(10)
                                    VStack{
                                        Text("BALANCE").foregroundColor(.white).fontWeight(.semibold).font(.system(size:20))
                                        HStack{
                                            Image(systemName: "indianrupeesign").foregroundColor(.green)
                                           Text("1500").foregroundColor(.green).font(.system(size:24))
                                        }
                                    }
                                }
                                
                                ZStack{
                                    Rectangle().frame(width:110,height:65).foregroundColor(.color).cornerRadius(10)
                                    VStack{
                                        Text("OWE").foregroundColor(.white).fontWeight(.semibold).font(.system(size:20))
                                        HStack{
                                            Image(systemName: "indianrupeesign").foregroundColor(.red)
                                            Text("900").foregroundColor(.red).font(.system(size:24))
                                        }
                                    }
                                    
                                }
                                
                                ZStack{
                                    Rectangle().frame(width:110,height:65).foregroundColor(.color).cornerRadius(10)
                                    VStack{
                                        Text("OWED").foregroundColor(.white).fontWeight(.semibold).font(.system(size:18))
                                        HStack{
                                            Image(systemName: "indianrupeesign").foregroundColor(.green)
                                            Text("1500").foregroundColor(.green).font(.system(size:24))
                                            
                                        }
                                    }
                                    
                                }
                                
                            }
                            
                        }.frame(width:340,height:230,alignment: .leading).padding(.bottom,10)
                        
                        
                    }
                    
                    ZStack{
                        Rectangle().frame(width:160,height:55).foregroundColor(.black).cornerRadius(10)
                        Label("Groups", systemImage: "person.3").font(.title2).foregroundColor(.white)
                    }.frame(width:360,height:60,alignment: .leading)
                    
                    HStack{
                        VStack{
                            Image("trip1")
                            Text("Delhi!").font(.title3).foregroundColor(.white)
                            Text("Settled Up").font(.caption).foregroundColor(.gray)
                        }
                        Spacer()
                        Text("Settled Up").font(.title).foregroundColor(.gray)
                         
                        
                        
                        
                    }.padding([.leading,.trailing],25)
                    
                    HStack{
                        VStack{
                            Image("trip2")
                            Text("Manali!").font(.title3).foregroundColor(.white)
                            Text("Owe 25 INR").font(.caption).foregroundColor(.red)
                        }
                        
                        Spacer()
                        VStack{
                            HStack{
                                Text("You Owe").font(.title).foregroundColor(.red)
                                Label("25", systemImage: "indianrupeesign").foregroundColor(.red)
                            }
                            HStack{
                                Text("You owe Vaibhav K.").foregroundColor(.gray)
                                Label("25", systemImage: "indianrupeesign").foregroundColor(.red)
                                
                            }
                         
                            
                        }
                        
                    }.padding([.leading,.trailing],25)
                    
                    HStack{
                        VStack{
                            Image("trip3")
                            Text("IIT Ropar!").font(.title3).foregroundColor(.white)
                            Text("Owed 50 INR").font(.caption).foregroundColor(.green)
                        }
                        Spacer()
                        VStack{
                            HStack{
                                Text("You Owe").font(.title).foregroundColor(.green)
                                Label("25", systemImage: "indianrupeesign").foregroundColor(.green)
                                
                            }
                            
                            
                            HStack{
                                
                                Text("Irfan M Owes you").foregroundColor(.gray)
                                Label("25", systemImage: "indianrupeesign").foregroundColor(.green)
                                
                            }
                        }
                        
                         
                        
                        
                       
                    }.padding([.leading,.trailing],25)
                    
                    
                    
                    Spacer()
                }
            
            }
        }
    
}
            
            
            
#Preview {
    GroupsView()
}
