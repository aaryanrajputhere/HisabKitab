//
//  ContentView.swift
//  SPLITWISE
//
//  Created by Irfan on 23/02/24.
//

import SwiftUI
import SwiftData

struct ContentView: View {
    
    init() {
        UITabBar.appearance().backgroundColor = UIColor.black
        UITabBar.appearance().unselectedItemTintColor=UIColor.white

    }

    var body: some View {
        TabView{
            
            HomeView().tabItem { Label("Home", systemImage: "house") }
            
            GroupsView().font(.title).tabItem { Label("Groups",systemImage: "person.3").foregroundColor(.white) }
            
            Text("Friends").font(.title).tabItem{
                Label("Friends", systemImage: "person.badge.shield.checkmark")}
            
            Text("Profile").font(.title).tabItem{
                Label("Profile", systemImage: "person.circle")}
            
            
        }
        
    }
}

#Preview {
    ContentView()
        .modelContainer(for: Item.self, inMemory: true)
}
